
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Konfigurasi dashboard
st.set_page_config(
    page_title="E-Commerce Data Analysis",
    page_icon="🛒",
    layout="wide"
)

# Judul dashboard
st.title("🛒 E-Commerce Data Analysis Dashboard")
st.markdown(
    "Dashboard ini menampilkan hasil analisis data transaksi "
    "E-Commerce Public Dataset."
)

# Membaca dataset
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR.parent / "data"

orders_df = pd.read_csv(DATA_DIR / "orders_dataset.csv")
payments_df = pd.read_csv(DATA_DIR / "order_payments_dataset.csv")
customers_df = pd.read_csv(DATA_DIR / "customers_dataset.csv")

# Mengubah format tanggal
orders_df["order_purchase_timestamp"] = pd.to_datetime(
    orders_df["order_purchase_timestamp"],
    errors="coerce"
)

# Sidebar
st.sidebar.header("Filter Dashboard")

status_list = sorted(orders_df["order_status"].dropna().unique())

selected_status = st.sidebar.multiselect(
    "Pilih Status Pesanan",
    options=status_list,
    default=status_list
)

filtered_orders = orders_df[
    orders_df["order_status"].isin(selected_status)
]

# Metrics
total_orders = filtered_orders["order_id"].nunique()
total_customers = customers_df["customer_id"].nunique()
total_payments = payments_df["order_id"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Pesanan", f"{total_orders:,}")
col2.metric("Total Pelanggan", f"{total_customers:,}")
col3.metric("Pesanan dengan Pembayaran", f"{total_payments:,}")

st.divider()

# Grafik tren pesanan bulanan
st.subheader("📈 Tren Jumlah Pesanan E-Commerce Setiap Bulan")

monthly_orders = (
    filtered_orders
    .dropna(subset=["order_purchase_timestamp"])
    .groupby(
        filtered_orders["order_purchase_timestamp"]
        .dt.to_period("M")
    )["order_id"]
    .nunique()
)

monthly_orders.index = monthly_orders.index.astype(str)

fig, ax = plt.subplots(figsize=(12, 5))

monthly_orders.plot(
    kind="line",
    marker="o",
    ax=ax
)

ax.set_title("Tren Jumlah Pesanan per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pesanan")
ax.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

# Grafik metode pembayaran
st.subheader("💳 Metode Pembayaran yang Paling Banyak Digunakan")

payment_counts = payments_df["payment_type"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))

payment_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Distribusi Metode Pembayaran")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
ax.grid(axis="y", alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Tabel data
st.divider()

st.subheader("📋 Data Pesanan")

st.dataframe(
    filtered_orders.head(10),
    use_container_width=True
)

st.caption("Dashboard dibuat untuk Project Analisis Data Dicoding.")
