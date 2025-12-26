CREATE TABLE galeri_foto (
    id SERIAL PRIMARY KEY,
    nama_file TEXT,
    deskripsi_ai TEXT,
    tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);