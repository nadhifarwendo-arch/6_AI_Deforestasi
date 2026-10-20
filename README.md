# Studi Kasus Transkrip 6 — AI untuk Pemantauan Perubahan Hutan

## Ringkasan
Repositori ini dibuat berdasarkan materi kuliah praktisi oleh Dr. Bart Slaughter tentang penggunaan **remote sensing, data satelit multitemporal, dan kecerdasan buatan (AI)** untuk mengidentifikasi perubahan hutan tropis.

Materi membahas pemanfaatan data satelit seperti Sentinel-1 (radar) dan Sentinel-2 (optik), klasifikasi tutupan/perubahan lahan, tantangan awan pada citra optik, serta pentingnya validasi hasil. Data satelit dapat membantu mendeteksi pola perubahan, tetapi penyebab kehilangan hutan tidak selalu bisa ditentukan hanya dari citra; validasi lapangan dan konteks tambahan tetap penting.

## Studi kasus
**Masalah:** petugas pemantauan lingkungan menerima tabel hasil pengamatan beberapa lokasi hutan. Mereka perlu menyaring lokasi yang patut diperiksa lebih lanjut.

**Solusi demo:** melatih model Random Forest untuk mengklasifikasikan baris data sintetis menjadi `perlu_diperiksa` atau `normal` berdasarkan fitur contoh seperti perubahan indeks vegetasi, perubahan tutupan, kelembapan, dan indikasi gangguan.

> **Penting:** dataset pada folder `data/` adalah data sintetis untuk latihan pemrograman. Ini bukan citra satelit asli, bukan hasil penelitian Dr. Slaughter, dan bukan model operasional untuk mengambil keputusan lingkungan. Jangan gunakan hasilnya sebagai bukti deforestasi nyata.

## Struktur proyek
```text
.
├── README.md
├── requirements.txt
├── LICENSE
├── transkrip/
│   └── transkrip-6-ai-pemantauan-deforestasi.txt
├── data/
│   └── forest_change_demo.csv
└── src/
    └── classify_forest_change.py
```

## Persyaratan
- Python 3.10 atau lebih baru
- Paket: `pandas`, `scikit-learn`

## Menjalankan proyek
1. Ekstrak ZIP.
2. Buka terminal pada folder proyek.
3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan:
   ```bash
   python src/classify_forest_change.py
   ```

Skrip membagi data menjadi data latih dan data uji, melatih model Random Forest, lalu menampilkan classification report dan prediksi demo.

## Alur implementasi
1. Membaca dataset CSV.
2. Memisahkan fitur numerik dan label.
3. Membagi data latih/uji secara stratified.
4. Melatih `RandomForestClassifier`.
5. Mengevaluasi model pada data uji.
6. Menampilkan prediksi untuk contoh pengamatan baru.

## Pengembangan lanjutan
- Ganti dataset sintetis dengan data yang sah dan terdokumentasi.
- Gunakan citra Sentinel-1/Sentinel-2 yang sudah diproses dengan prosedur yang sesuai.
- Tambahkan data referensi/ground truth dan validasi lapangan.
- Laporkan metrik per kelas, ketidakpastian, dan potensi bias.
- Jangan menyimpulkan penyebab perubahan hutan dari klasifikasi citra saja.

## Mengunggah ke GitHub
1. Buat repositori baru di https://github.com/new.
2. Ekstrak ZIP ini.
3. Unggah **isi folder proyek** (bukan ZIP-nya saja) melalui **Add file → Upload files**.
4. Isi pesan commit, misalnya `Add study case AI forest monitoring`.
5. Klik **Commit changes**.

## Sumber materi
Transkrip yang disertakan merupakan sumber materi diskusi. Implementasi kode dan dataset demo dibuat untuk tujuan pembelajaran dan tidak diklaim sebagai kode atau dataset dari pemateri.
