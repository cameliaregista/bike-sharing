# Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis pola penyewaan sepeda berdasarkan waktu, musim, cuaca, dan karakteristik hari menggunakan Streamlit.

## Setup Environment

### Menggunakan virtual environment (disarankan)

```bash
python -m venv .venv
```

Aktifkan virtual environment:

- Windows (PowerShell):
  ```bash
  .\.venv\Scripts\Activate.ps1
  ```

- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

## Install Dependencies

Pastikan file `requirements.txt` berada pada root project, kemudian jalankan:

```bash
pip install -r requirements.txt
```

## Menjalankan Dashboard Secara Lokal

Jalankan perintah berikut dari direktori project:

```bash
streamlit run dashboard.py
```

Setelah server berjalan, buka URL yang ditampilkan pada terminal (biasanya `http://localhost:8501`) di browser.

## Struktur Proyek

```text
├── dashboard.py
├── requirements.txt
├── data/
│   └── bike_sharing.csv
└── README.md
```

Sesuaikan nama file data atau script utama apabila berbeda dengan struktur 