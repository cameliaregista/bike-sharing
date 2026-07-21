# Bike Sharing Dashboard

Dashboard interaktif yang dibuat menggunakan Streamlit untuk menganalisis pola penyewaan sepeda berdasarkan kondisi cuaca, musim, serta pola penggunaan berdasarkan waktu.

Project ini menggunakan Bike Sharing Dataset tahun 2011–2012 untuk memahami tren penyewaan sepeda dan menghasilkan insight yang dapat membantu pengambilan keputusan operasional, seperti perencanaan jumlah sepeda dan optimasi ketersediaan layanan.

---

## Gambaran Project

Layanan bike sharing perlu memahami perilaku pengguna dan pola permintaan agar operasional dapat berjalan lebih efektif.

Dashboard ini berfokus pada analisis:

- Performa penyewaan sepeda secara keseluruhan
- Pengaruh kondisi cuaca terhadap jumlah penyewaan
- Pola penyewaan berdasarkan jam pada hari kerja dan hari libur
- Rekomendasi bisnis berdasarkan hasil analisis data

---

## Fitur Dashboard

### 1. Ringkasan Performa Penyewaan

Dashboard menampilkan beberapa metrik utama:

- Total penyewaan sepeda
- Rata-rata penyewaan
- Jumlah penyewaan maksimum

Pengguna dapat melakukan filter berdasarkan musim untuk melihat perbedaan pola penyewaan.

---

### 2. Rata-rata Penyewaan Berdasarkan Kondisi Cuaca

Pertanyaan Bisnis:

Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?

Insight:

- Kondisi cuaca cerah menghasilkan rata-rata penyewaan tertinggi.
- Kondisi cuaca yang kurang baik cenderung menurunkan jumlah pengguna.

---

### 3. Pola Penyewaan Berdasarkan Jam

Pertanyaan Bisnis:

Kapan waktu dengan permintaan penyewaan tertinggi pada hari kerja dan hari libur?

Insight:

- Hari kerja memiliki pola peningkatan permintaan pada jam sibuk:
  - 07.00–09.00
  - 16.00–18.00

- Hari libur memiliki pola penyewaan yang lebih merata dengan peningkatan penggunaan pada siang hari.

---

## Teknologi yang Digunakan

Project ini menggunakan:

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

---

## Struktur Project

```
Bike-Sharing-Dashboard/
│
├── data/
│   ├── day.csv
│   └── hour.csv
│
├── dashboard.py
│
├── requirements.txt
│
└── README.md
```

---

## Setup Environment

Ikuti langkah berikut untuk menjalankan dashboard secara lokal.

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/bike-sharing-dashboard.git
```

Masuk ke folder project:

```bash
cd bike-sharing-dashboard
```

---

### 2. Membuat Virtual Environment

Buat virtual environment menggunakan Python:

```bash
python -m venv venv
```

Aktifkan virtual environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Library

Install seluruh library yang dibutuhkan berdasarkan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

Library utama yang digunakan:

```txt
streamlit==1.59.2
pandas==3.0.3
matplotlib==3.11.1
seaborn==0.13.2
```

---

## Menjalankan Dashboard Secara Lokal

Jalankan perintah berikut:

```bash
streamlit run dashboard.py
```

Dashboard dapat diakses melalui browser pada:

```
http://localhost:8501
```

---

## Dataset

Project ini menggunakan Bike Sharing Dataset yang berisi data penyewaan sepeda secara harian dan per jam.

File dataset:

- `day.csv`
- `hour.csv`

Dataset mencakup informasi:

- Tanggal
- Musim
- Kondisi cuaca
- Status hari kerja
- Temperatur
- Jumlah penyewaan sepeda

---

## Rekomendasi Bisnis

Berdasarkan hasil analisis, beberapa rekomendasi yang dapat diberikan:

- Menambah ketersediaan sepeda pada jam sibuk, terutama saat jam berangkat dan pulang kerja.
- Melakukan redistribusi sepeda berdasarkan pola permintaan pengguna.
- Membuat strategi promosi pada kondisi cuaca kurang mendukung untuk mempertahankan penggunaan layanan.

---

## Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

- Menambahkan analisis tren penyewaan berdasarkan bulan dan tahun.
- Menggunakan visualisasi interaktif dengan Plotly.
- Membuat model prediksi jumlah penyewaan sepeda.
- Menambahkan analisis berdasarkan lokasi atau stasiun sepeda.

---

## Author

Camelia Regista

Data Analytics Portfolio Project