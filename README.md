<div align="center">

# 🖼️ AI Smart Gallery
### **Intelligent Image Description with Azure Computer Vision**

![Python](https://img.shields.io/badge/Language-Python%203-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-000000?logo=flask&logoColor=white)
![Azure](https://img.shields.io/badge/AI-Azure%20Computer%20Vision-0078D4?logo=microsoft-azure&logoColor=white)

<br/>

<p align="center">
  <b>Upload Photo</b> • <b>AI Analysis</b> • <b>Get Description</b>
</p>

</div>

---

## 📝 Overview
**AI Smart Gallery** adalah aplikasi web sederhana namun canggih yang dibangun menggunakan **Python Flask**. Aplikasi ini terintegrasi dengan **Azure Computer Vision API** untuk menganalisis gambar yang diunggah dan menghasilkan deskripsi (caption) yang akurat secara otomatis.

Project ini dibuat untuk mendemonstrasikan bagaimana *Artificial Intelligence* dapat "melihat" dan memahami konteks sebuah foto.

---

## ✨ Key Features
* 📤 **Easy Upload:** Antarmuka sederhana untuk mengunggah gambar.
* 🤖 **AI Description:** Menggunakan Azure Cognitive Services untuk mendeskripsikan isi gambar.
* 🏷️ **Confidence Score:** Menampilkan tingkat keyakinan (akurasi) dari tebakan AI.
* ⚡ **Fast Processing:** Ringan dan cepat dengan framework Flask.

---

## 🛠️ Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) | Web framework Python yang ringan. |
| **AI Cloud** | ![Azure](https://img.shields.io/badge/-Azure%20Cognitive-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white) | Computer Vision API untuk analisis gambar. |
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Bahasa pemrograman utama. |
| **Frontend** | HTML/CSS | Template antarmuka sederhana (Jinja2). |

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Akun Microsoft Azure (untuk mendapatkan API Key & Endpoint)

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/ivanfauz/ai-smart-gallery.git](https://github.com/ivanfauz/ai-smart-gallery.git)
    cd ai-smart-gallery
    ```

2.  **Install Dependencies**
    ```bash
    pip install flask azure-cognitiveservices-vision-computervision msrest
    ```

3.  **Setup Environment Variables**
    Buat file `.env` atau atur langsung di kode (tidak disarankan untuk production) untuk menyimpan kredensial Azure:
    ```bash
    AZURE_VISION_KEY="masukkan_key_azure_disini"
    AZURE_VISION_ENDPOINT="masukkan_endpoint_azure_disini"
    ```

4.  **Run the App**
    ```bash
    python app.py
    ```

5.  **Access the App**
    Buka browser dan akses: `http://localhost:5000`

---

## 📸 How It Works
1. User mengunggah foto pemandangan/objek.
2. Flask mengirimkan gambar ke Azure Computer Vision.
3. Azure mengembalikan teks deskripsi (contoh: *"a person riding a bicycle on a busy street"*).
4. Hasil ditampilkan di halaman web.

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/ivanfauz">Ivan Fauzan</a>
</div>
