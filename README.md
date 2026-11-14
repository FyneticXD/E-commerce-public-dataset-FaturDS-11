# E-Commerce Data Analysis Dashboard 📊

## Deskripsi Project

Project ini merupakan tugas akhir dari course **Belajar Fundamental Analisis Data** di Dicoding.

Project ini bertujuan untuk menganalisis data transaksi E-Commerce menggunakan E-Commerce Public Dataset dari Olist. Analisis dilakukan untuk memahami tren jumlah pesanan, nilai pembayaran, dan metode pembayaran pelanggan.

Hasil analisis disajikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Business Questions

Analisis ini berfokus pada beberapa pertanyaan bisnis berikut:

1. **Bagaimana tren jumlah pesanan E-Commerce setiap bulan selama periode 4 September 2016 hingga 17 Oktober 2018?**
2. **Metode pembayaran apa yang paling banyak digunakan pelanggan dan bagaimana proporsi penggunaannya dibandingkan metode pembayaran lainnya?**
3. **Bagaimana tren total nilai pembayaran setiap bulan selama periode data yang tersedia?**

## Features

Dashboard memiliki beberapa fitur utama:

- **Filter Status Pesanan** – Memfilter data berdasarkan status pesanan.
- **Total Pesanan** – Menampilkan jumlah pesanan berdasarkan filter yang dipilih.
- **Total Pelanggan** – Menampilkan jumlah pelanggan pada data pesanan yang difilter.
- **Total Nilai Pembayaran** – Menampilkan total nilai pembayaran dari pesanan yang difilter.
- **Tren Jumlah Pesanan Bulanan** – Menampilkan perubahan jumlah pesanan setiap bulan.
- **Tren Nilai Pembayaran Bulanan** – Menampilkan perubahan total nilai pembayaran setiap bulan.
- **Distribusi Metode Pembayaran** – Menampilkan jumlah transaksi berdasarkan metode pembayaran.
- **Proporsi Metode Pembayaran** – Menampilkan persentase penggunaan setiap metode pembayaran.
- **Data Pesanan** – Menampilkan tabel data pesanan.

## Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit

## Project Structure

```text
E-commerce-public-dataset-FaturDS-11/
├── dashboard/
│   └── dashboard.py
├── data/
│   ├── customers_dataset.csv
│   ├── order_payments_dataset.csv
│   └── orders_dataset.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/FyneticXD/E-commerce-public-dataset-FaturDS-11.git
```

### 2. Navigate to Project Directory

```bash
cd E-commerce-public-dataset-FaturDS-11
```

### 3. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

Dashboard akan terbuka melalui browser pada alamat:

```text
http://localhost:8501
```

## Dataset

Dataset yang digunakan adalah **E-Commerce Public Dataset** dari Olist.

Dataset yang digunakan pada dashboard meliputi:

- `orders_dataset.csv`
- `order_payments_dataset.csv`
- `customers_dataset.csv`

Dataset ini digunakan untuk menganalisis aktivitas pesanan, nilai pembayaran, dan metode pembayaran pelanggan.

## Dashboard Preview

Dashboard dapat diakses melalui link berikut:

[ E-Commerce Data Analysis Dashboard ](https://olist-ecommerce-dashboard-fyneticxd.streamlit.app/)

Dashboard menampilkan tren jumlah pesanan bulanan, tren nilai pembayaran, distribusi metode pembayaran, proporsi metode pembayaran, serta tabel data pesanan.

## Author

**Fatur Rachman Putra Nanta Efendi**

Information Systems Student  
Universitas Pembangunan Nasional "Veteran" Jawa Timur

---

Project ini dibuat sebagai bagian dari tugas akhir Dicoding – Belajar Fundamental Analisis Data.
