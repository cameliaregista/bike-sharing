# 🚲 Dashboard Analisis Bike Sharing

Dashboard interaktif yang dibuat menggunakan **Streamlit** untuk menganalisis pola penyewaan sepeda berdasarkan musim, kondisi cuaca, hari kerja, dan waktu penyewaan.

Project ini menggunakan **Bike Sharing Dataset tahun 2011–2012** untuk memahami pola permintaan penyewaan sepeda serta menghasilkan insight yang dapat mendukung pengambilan keputusan operasional, seperti perencanaan ketersediaan sepeda dan optimalisasi layanan.

---

## 📌 Gambaran Project

Layanan penyewaan sepeda perlu memahami pola permintaan dan perilaku pengguna agar ketersediaan sepeda dapat disesuaikan dengan kebutuhan.

Dashboard ini berfokus pada beberapa aspek utama:

* Performa penyewaan sepeda secara keseluruhan
* Pola penyewaan berdasarkan musim
* Pengaruh kondisi cuaca terhadap jumlah penyewaan
* Pola penyewaan berdasarkan jam
* Perbandingan penyewaan pada hari kerja dan bukan hari kerja
* Distribusi penyewaan berdasarkan temperatur dan kondisi cuaca
* Rekomendasi bisnis berdasarkan hasil analisis data

---

## 🎯 Pertanyaan Bisnis

### 1. Bagaimana performa penyewaan sepeda secara keseluruhan?

Dashboard menampilkan tiga indikator utama:

* **Total Penyewaan** — jumlah keseluruhan sepeda yang disewa
* **Rata-rata Penyewaan** — rata-rata jumlah penyewaan
* **Penyewaan Maksimum** — jumlah penyewaan tertinggi

Dashboard juga menyediakan filter berdasarkan **musim** untuk melihat perubahan performa penyewaan.

---

### 2. Bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda?

Analisis dilakukan untuk melihat hubungan antara kondisi cuaca dengan jumlah penyewaan sepeda.

**Insight:**

* Kondisi cuaca cerah menghasilkan rata-rata penyewaan yang lebih tinggi.
* Kondisi cuaca yang kurang baik seperti kabut atau hujan cenderung memiliki jumlah penyewaan yang lebih rendah.

Hal ini menunjukkan bahwa **kondisi cuaca merupakan salah satu faktor yang berkaitan dengan tingkat permintaan penyewaan sepeda**.

---

### 3. Kapan waktu dengan permintaan penyewaan tertinggi?

Analisis pola penyewaan berdasarkan jam dilakukan dengan membandingkan hari kerja dan bukan hari kerja.

Pada hari kerja, peningkatan permintaan terlihat terutama pada jam sibuk:

* **07.00–09.00**
* **16.00–18.00**

Sementara itu, pada hari bukan kerja, pola penyewaan cenderung lebih merata dan meningkat pada siang hari.

---

### 4. Bagaimana distribusi penyewaan harian berdasarkan temperatur dan kondisi cuaca?

Analisis pada tingkat harian menunjukkan bahwa jumlah penyewaan yang tinggi lebih banyak ditemukan pada kondisi cuaca **cerah**.

Sebaliknya, kondisi **hujan** atau **kabut** lebih banyak ditemukan pada tingkat penyewaan yang relatif rendah.

Hal tersebut semakin menunjukkan adanya hubungan antara **kondisi cuaca dan tingkat permintaan penyewaan sepeda**.

---

## 📊 Fitur Dashboard

### 1. Ringkasan Performa Penyewaan

Dashboard menampilkan tiga indikator utama:

* Total Penyewaan
* Rata-rata Penyewaan
* Penyewaan Maksimum

Nilai indikator akan berubah secara otomatis berdasarkan musim yang dipilih.

---

### 2. Filter Musim

Dashboard menggunakan **Single Select Box** sebagai filter.

Pilihan yang tersedia:

* `All`
* `Fall`
* `Spring`
* `Summer`
* `Winter`

Filter default adalah **`All`**, sehingga ketika dashboard pertama kali dibuka, seluruh data akan ditampilkan.

---

### 3. Analisis Kondisi Cuaca

Menampilkan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca.

Visualisasi ini digunakan untuk melihat bagaimana perubahan kondisi cuaca berkaitan dengan tingkat permintaan penyewaan.

---

### 4. Pola Penyewaan Berdasarkan Jam

Menampilkan pola rata-rata penyewaan berdasarkan jam serta membandingkan:

* Hari kerja
* Bukan hari kerja

Analisis ini membantu mengidentifikasi periode dengan permintaan penyewaan yang tinggi.

---

### 5. Perbandingan Pengguna

Menampilkan perbandingan jumlah penyewaan berdasarkan jenis pengguna:

* **Pengguna Kasual**
* **Pengguna Terdaftar**

---

### 6. Analisis Berdasarkan Hari

Menampilkan rata-rata jumlah penyewaan berdasarkan hari dalam satu minggu.

---

### 7. Tren Penyewaan dari Waktu ke Waktu

Menampilkan perubahan jumlah penyewaan harian untuk melihat pola dan tren permintaan selama periode pengamatan.

---

## 🛠️ Teknologi yang Digunakan

Project ini dibuat menggunakan:

* **Python**
* **Pandas**
* **Streamlit**
* **Matplotlib**
* **Seaborn**

---

## 📂 Struktur Project

```text
Bike-Sharing-Dashboard/
│
├── .devcontainer/
│
├── data/
│   ├── day.csv
│   ├── hour.csv
│   └── main_data.csv
│
├── venv/
│
├── .gitignore
│
├── dashboard.py
│
├── requirements.txt
│
├── README.md
│
└── Submission_Fundamental_Analisis_Data/
```

### Penjelasan File dan Folder

| File/Folder        | Keterangan                                               |
| ------------------ | -------------------------------------------------------- |
| `data/`            | Folder yang berisi dataset asli                          |
| `day.csv`          | Dataset penyewaan sepeda pada tingkat harian             |
| `hour.csv`         | Dataset penyewaan sepeda pada tingkat per jam            |
| `main_data.csv`    | Dataset yang telah diproses dan digunakan oleh dashboard |
| `dashboard.py`     | Kode utama aplikasi Streamlit                            |
| `requirements.txt` | Daftar library yang dibutuhkan                           |
| `README.md`        | Dokumentasi project                                      |
| `venv/`            | Lingkungan virtual Python                                |

> **Catatan:** Folder `venv/` digunakan untuk lingkungan virtual Python dan tidak perlu dimasukkan ke dalam repository GitHub.

---

## ⚙️ Persiapan Lingkungan

Ikuti langkah berikut untuk menjalankan dashboard secara lokal.

### 1. Clone Repository

Clone repository menggunakan Git:

```bash
git clone https://github.com/yourusername/bike-sharing-dashboard.git
```

Kemudian masuk ke folder project:

```bash
cd bike-sharing-dashboard
```

---

### 2. Membuat Lingkungan Virtual

Buat lingkungan virtual menggunakan Python:

```bash
python -m venv venv
```

Aktifkan lingkungan virtual.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Memasang Library

Pasang seluruh library yang dibutuhkan menggunakan:

```bash
pip install -r requirements.txt
```

Library utama yang digunakan:

```text
streamlit==1.59.2
pandas==2.2.3
mmatplotlib==3.10.0
seaborn==0.13.2
```

---

## ▶️ Menjalankan Dashboard

Pastikan `main_data.csv` berada pada folder data.

```text
Bike-Sharing-Dashboard/
│
├── dashboard.py
├── data
├────main_data.csv
└── ...
```

Kemudian jalankan perintah:

```bash
streamlit run dashboard.py
```

Setelah berhasil dijalankan, dashboard dapat diakses melalui:

```text
http://localhost:8501
```

---

## 📁 Dataset

Project ini menggunakan **Bike Sharing Dataset tahun 2011–2012**.

Dataset awal terdiri dari:

* `day.csv`
* `hour.csv`

Dataset mencakup informasi mengenai:

* Tanggal
* Musim
* Kondisi cuaca
* Hari kerja
* Temperatur
* Kelembapan
* Kecepatan angin
* Pengguna kasual
* Pengguna terdaftar
* Total penyewaan sepeda

Dataset yang digunakan secara langsung oleh dashboard adalah:

```text
main_data.csv
```

`main_data.csv` merupakan dataset yang telah diproses dan digunakan sebagai sumber data utama aplikasi Streamlit.

---

## 💡 Insight Utama

Berdasarkan hasil analisis data, beberapa insight yang diperoleh adalah:

### ☀️ 1. Kondisi Cuaca Berkaitan dengan Tingkat Penyewaan

Penyewaan sepeda cenderung lebih tinggi ketika kondisi cuaca cerah.

Sebaliknya, kondisi cuaca seperti kabut dan hujan cenderung memiliki tingkat penyewaan yang lebih rendah.

---

### 🕐 2. Permintaan Meningkat pada Jam Sibuk

Pada hari kerja, terdapat peningkatan permintaan terutama pada jam pagi dan sore.

Pola tersebut berkaitan dengan waktu perjalanan pengguna, seperti perjalanan menuju dan pulang dari aktivitas sehari-hari.

---

### 👥 3. Pengguna Terdaftar Memberikan Kontribusi Besar

Pengguna terdaftar memberikan kontribusi yang signifikan terhadap keseluruhan jumlah penyewaan sepeda.

Hal ini menunjukkan pentingnya mempertahankan dan meningkatkan keterlibatan pengguna terdaftar.

---

### 🌦️ 4. Cuaca Perlu Dipertimbangkan dalam Perencanaan Operasional

Kondisi cuaca dapat menjadi salah satu faktor yang perlu diperhatikan ketika melakukan perencanaan permintaan dan ketersediaan sepeda.

---

## 💼 Rekomendasi Bisnis

Berdasarkan hasil analisis, beberapa rekomendasi yang dapat diberikan adalah:

### 1. Mengoptimalkan Ketersediaan Sepeda

Meningkatkan ketersediaan sepeda pada periode dengan permintaan tinggi, terutama pada jam sibuk di hari kerja.

### 2. Melakukan Redistribusi Sepeda

Melakukan redistribusi sepeda berdasarkan pola permintaan historis agar ketersediaan sepeda dapat mengikuti kebutuhan pengguna.

### 3. Mempertimbangkan Kondisi Cuaca

Informasi cuaca dapat digunakan sebagai salah satu faktor dalam memperkirakan tingkat permintaan harian.

### 4. Membuat Strategi Promosi

Promosi dapat dipertimbangkan pada periode dengan permintaan rendah untuk membantu meningkatkan penggunaan layanan.

---

## 🚀 Pengembangan Selanjutnya

Project ini masih dapat dikembangkan lebih lanjut dengan:

* Menambahkan analisis tren berdasarkan bulan dan tahun
* Menggunakan visualisasi interaktif dengan Plotly
* Menambahkan analisis prediksi jumlah penyewaan
* Membuat model peramalan permintaan
* Menambahkan analisis berdasarkan lokasi atau stasiun
* Menambahkan filter berdasarkan tahun dan bulan
* Meningkatkan desain dan pengalaman pengguna dashboard
* Melakukan deployment dashboard secara online

---

## 👩‍💻 Penulis

**Camelia Regista**

*Data Analytics Portfolio Project*
