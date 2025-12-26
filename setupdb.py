import psycopg2

# --- SAMAKAN INI DENGAN DATA DI APP.PY ANDA ---
DB_HOST = "db-gallery-ivan.postgres.database.azure.com"
DB_USER = "adminuser"      # Ganti jika user anda beda
DB_PASS = "Rahasia123!"    # Ganti dengan password anda
DB_NAME = "postgres"

def create_table():
    try:
        # Konek ke database
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = conn.cursor()
        
        # Perintah bikin tabel
        print("Sedang membuat tabel galeri_foto...")
        create_query = """
        CREATE TABLE IF NOT EXISTS galeri_foto (
            id SERIAL PRIMARY KEY,
            nama_file TEXT,
            deskripsi_ai TEXT,
            tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        cur.execute(create_query)
        conn.commit()
        
        print("BERHASIL! Tabel 'galeri_foto' sudah dibuat.")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print("Terjadi Error:", e)

if __name__ == "__main__":
    create_table()