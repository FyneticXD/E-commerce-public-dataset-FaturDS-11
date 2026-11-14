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
    """
    Dashboard ini menyajikan analisis jumlah pesanan, tren nilai pembayaran,
    dan metode pembayaran pada E-Commerce Public Dataset.
    """
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

# Sidebar filter
st.sidebar.header("Filter Dashboard")

status_list = sorted(orders_df["order_status"].dropna().unique())

selected_status = st.sidebar.multiselect(
    "Pilih Status Pesanan",
    options=status_list,
    default=status_list
)

# Filter pesanan
filtered_orders = orders_df[
    orders_df["order_status"].isin(selected_status)
].copy()

# Filter pembayaran sesuai pesanan
filtered_order_ids = filtered_orders["order_id"].unique()

filtered_payments = payments_df[
    payments_df["order_id"].isin(filtered_order_ids)
].copy()

# KPI
total_orders = filtered_orders["order_id"].nunique()
total_customers = filtered_orders["customer_id"].nunique()
total_payment_value = filtered_payments["payment_value"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Pesanan", f"{total_orders:,}")
col2.metric("Total Pelanggan", f"{total_customers:,}")
col3.metric("Total Nilai Pembayaran", f"R$ {total_payment_value:,.2f}")

st.divider()

# Grafik tren jumlah pesanan bulanan
st.subheader("📈 Tren Jumlah Pesanan Setiap Bulan")

monthly_orders = (
    filtered_orders
    .dropna(subset=["order_purchase_timestamp"])
    .groupby(
        filtered_orders["order_purchase_timestamp"].dt.to_period("M")
    )["order_id"]
    .nunique()
)

monthly_orders.index = monthly_orders.index.astype(str)

fig, ax = plt.subplots(figsize=(12, 5))
monthly_orders.plot(kind="line", marker="o", ax=ax)

ax.set_title("Tren Jumlah Pesanan per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Pesanan")
ax.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

# Grafik tren nilai pembayaran bulanan
st.subheader("💰 Tren Nilai Pembayaran Setiap Bulan")

payment_orders = filtered_orders[
    ["order_id", "order_purchase_timestamp"]
].dropna()

monthly_payment_data = filtered_payments.merge(
    payment_orders,
    on="order_id",
    how="inner"
)

monthly_payment_data["Bulan"] = (
    monthly_payment_data["order_purchase_timestamp"].dt.to_period("M")
)

monthly_revenue = monthly_payment_data.groupby("Bulan")[
    "payment_value"
].sum()

monthly_revenue.index = monthly_revenue.index.astype(str)

fig, ax = plt.subplots(figsize=(12, 5))
monthly_revenue.plot(kind="line", marker="o", ax=ax)

ax.set_title("Tren Total Nilai Pembayaran per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Pembayaran (R$)")
ax.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

# Grafik metode pembayaran
st.subheader("💳 Distribusi Metode Pembayaran")

payment_counts = filtered_payments["payment_type"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
payment_counts.plot(kind="bar", ax=ax)

ax.set_title("Jumlah Transaksi Berdasarkan Metode Pembayaran")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
ax.grid(axis="y", alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Proporsi metode pembayaran
st.subheader("📊 Proporsi Metode Pembayaran")

payment_proportion = (
    filtered_payments["payment_type"]
    .value_counts(normalize=True)
    .mul(100)
)

st.dataframe(
    payment_proportion.rename("Persentase (%)").round(2),
    use_container_width=True
)

st.divider()

# Tabel data pesanan
st.subheader("📋 Data Pesanan")

st.dataframe(
    filtered_orders.head(10),
    use_container_width=True
)

st.caption("Dashboard dibuat untuk Project Analisis Data Dicoding.")