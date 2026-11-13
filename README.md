
# Olist E-Commerce Data Analysis

## Deskripsi
Proyek ini merupakan analisis data pada Olist Brazilian
E-Commerce Public Dataset untuk memahami tren penjualan,
performa kategori produk, dan perilaku pelanggan.

## Analisis
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Analisis tren penjualan bulanan
- Analisis kategori produk
- RFM Analysis
- Segmentasi pelanggan
- Dashboard interaktif menggunakan Streamlit

## Struktur Folder

submission/
├── dashboard/
│   ├── dashboard.py
│   └── data/
│       ├── main_data.csv
│       ├── monthly_sales.csv
│       ├── category_sales.csv
│       ├── rfm_data.csv
│       └── segment_counts.csv
├── notebook.ipynb
├── README.md
└── requirements.txt

## Cara Menjalankan Dashboard

1. Install Python.
2. Buka terminal pada folder dashboard.
3. Install library:

   pip install -r ../requirements.txt

4. Jalankan dashboard:

   streamlit run dashboard.py

5. Dashboard akan terbuka di browser.

## Dataset
Olist Brazilian E-Commerce Public Dataset
