import os
from flask import Flask, render_template, request, redirect, url_for
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import psycopg2
from werkzeug.utils import secure_filename

app = Flask(__name__)

# --- KONFIGURASI (GANTI INI DENGAN DATA ANDA) ---
KEY = "rahasia"
ENDPOINT = "https://ai-gallery-ivan.cognitiveservices.azure.com/"
DB_HOST = "db-gallery-ivan.postgres.database.azure.com"
DB_USER = "adminuser"
DB_PASS = "Rahasia123!"
DB_NAME = "postgres"

# Konfigurasi Upload Folder
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- KONEKSI KE AZURE AI ---
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def get_db_connection():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
        return conn
    except Exception as e:
        print(f"Warning: could not connect to DB: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Ambil file gambar dari form
        file = request.files['image']
        if file and file.filename:
            filename = secure_filename(file.filename or "uploaded_image")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # 2. Kirim ke Azure Computer Vision
            # Kita buka file yang barusan diupload untuk dibaca AI
            with open(filepath, "rb") as image_stream:
                description_result = computervision_client.describe_image_in_stream(image_stream)  # type: ignore

            # Ambil caption terbaik dari AI, handle if captions is missing or None
            caption_ai = "Tidak ada deskripsi terdeteksi."
            # type: ignore digunakan untuk menghindari error Pyright pada atribut dinamis
            if hasattr(description_result, "captions") and getattr(description_result, "captions", None):  # type: ignore
                captions = getattr(description_result, "captions", [])  # type: ignore
                if len(captions) > 0 and hasattr(captions[0], "text"):
                    caption_ai = captions[0].text

            # 3. Simpan ke Database (jika tersedia)
            conn = get_db_connection()
            if conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO galeri_foto (nama_file, deskripsi_ai) VALUES (%s, %s)",
                            (filename, caption_ai))
                conn.commit()
                cur.close()
                conn.close()
            else:
                print("Info: database tidak tersedia — melewatkan penyimpanan.")
            
            return redirect(url_for('index'))

    # 4. Tampilkan Data dari Database
    conn = get_db_connection()
    photos = []
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM galeri_foto ORDER BY id DESC")
        photos = cur.fetchall()
        cur.close()
        conn.close()
    else:
        print("Info: database tidak tersedia — menampilkan galeri kosong.")

    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)