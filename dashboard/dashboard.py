
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

# Membaca data
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

df = pd.read_csv(os.path.join(DATA_DIR, "main_data.csv"))
category_sales = pd.read_csv(
    os.path.join(DATA_DIR, "category_sales.csv")
)
segment_counts = pd.read_csv(
    os.path.join(DATA_DIR, "segment_counts.csv")
)

# Mengubah tipe data tanggal
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"],
    errors="coerce"
)

# Judul dashboard
st.title("📊 Olist E-Commerce Dashboard")
st.caption(
    "Dashboard analisis penjualan dan perilaku pelanggan "
    "Olist periode 2017–2018"
)

# Sidebar filter tanggal
st.sidebar.header("Filter Data")

min_date = df["order_purchase_timestamp"].min().date()
max_date = df["order_purchase_timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Pilih rentang tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = df[
        (df["order_purchase_timestamp"].dt.date >= start_date) &
        (df["order_purchase_timestamp"].dt.date <= end_date)
    ].copy()
else:
    filtered_df = df.copy()

# Menghitung KPI
total_revenue = filtered_df["price"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_unique_id"].nunique()

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    f"R$ {total_revenue:,.2f}"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Total Customers",
    f"{total_customers:,}"
)

st.divider()

# Grafik tren penjualan bulanan
st.subheader("Tren Penjualan Bulanan")

monthly_data = filtered_df.groupby(
    filtered_df["order_purchase_timestamp"].dt.to_period("M")
).agg(
    total_orders=("order_id", "nunique"),
    total_revenue=("price", "sum")
).reset_index()

monthly_data["month"] = (
    monthly_data["order_purchase_timestamp"].astype(str)
)

fig_monthly = px.line(
    monthly_data,
    x="month",
    y="total_revenue",
    markers=True,
    title="Total Revenue per Bulan",
    labels={
        "month": "Bulan",
        "total_revenue": "Revenue (BRL)"
    }
)

st.plotly_chart(fig_monthly, use_container_width=True)

# Grafik kategori produk
st.subheader("Performa Kategori Produk")

top_category = category_sales.sort_values(
    "total_revenue",
    ascending=False
).head(10)

fig_category = px.bar(
    top_category,
    x="total_revenue",
    y="product_category_name",
    orientation="h",
    title="Top 10 Kategori Berdasarkan Revenue",
    labels={
        "total_revenue": "Revenue (BRL)",
        "product_category_name": "Kategori Produk"
    }
)

fig_category.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig_category, use_container_width=True)

# Grafik segmentasi pelanggan
st.subheader("Segmentasi Pelanggan RFM")

fig_segment = px.bar(
    segment_counts,
    x="Customer_Segment",
    y="Total_Customers",
    title="Distribusi Segmentasi Pelanggan",
    labels={
        "Customer_Segment": "Segmen Pelanggan",
        "Total_Customers": "Jumlah Pelanggan"
    }
)

st.plotly_chart(fig_segment, use_container_width=True)

# Tabel data
st.subheader("Detail Data Penjualan")

st.dataframe(
    filtered_df[
        [
            "order_id",
            "customer_unique_id",
            "order_purchase_timestamp",
            "product_category_name",
            "price"
        ]
    ].head(100),
    use_container_width=True
)

st.caption(
    "Data bersumber dari Olist Brazilian E-Commerce Public Dataset."
)
