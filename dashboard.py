import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- GATHERING DATA ----
st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚲")

# Load dataset yang sudah dibersihkan
day_df = pd.read_csv("clean_day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

hour_df = pd.read_csv("clean_hour.csv")
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar untuk filter
st.sidebar.header("🔍 Filter Data")

# ---- KETERANGAN MUSIM ----
st.sidebar.markdown("### 🌤️ Keterangan Musim:")
st.sidebar.markdown("""
- **1 (Musim Semi 🌱)**
- **2 (Musim Panas ☀️)** 
- **3 (Musim Gugur 🍂)**
""")

# Filter berdasarkan kondisi cuaca
selected_weathersit = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    day_df["weathersit"].unique(),
    default=day_df["weathersit"].unique()
)

# Filter berdasarkan rentang waktu (jam)
selected_hours = st.sidebar.slider(
    "Pilih Rentang Waktu (Jam):",
    min_value=0,
    max_value=23,
    value=(6, 22)
)

# Filter data berdasarkan input pengguna
filtered_day_df = day_df[day_df["weathersit"].isin(selected_weathersit)]
filtered_hour_df = hour_df[
    (hour_df["weathersit"].isin(selected_weathersit)) & 
    (hour_df["hr"] >= selected_hours[0]) & (hour_df["hr"] <= selected_hours[1])
]

# ---- VISUALISASI 1: Pengaruh Cuaca terhadap Penyewaan Sepeda (Bar Chart) ----
st.subheader("☁️ Pengaruh Cuaca terhadap Rata-rata Penyewaan Sepeda")

# Menghitung rata-rata jumlah penyewaan sepeda untuk setiap kondisi cuaca
weather_summary = filtered_day_df.groupby('weathersit')['cnt'].mean().reset_index()

# Mapping nilai weathersit ke label yang lebih deskriptif
weather_labels = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Hujan Lebat'
}
weather_summary['weathersit_label'] = weather_summary['weathersit'].map(weather_labels)

# Visualisasi menggunakan bar chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(weather_summary['weathersit_label'], weather_summary['cnt'], color='skyblue')

# Menambahkan label dan judul
ax.set_xlabel("Cuaca")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda")
ax.set_title("Pengaruh Cuaca terhadap Rata-rata Jumlah Penyewaan Sepeda")

# Menampilkan grafik
st.pyplot(fig)

# ---- VISUALISASI 2: Distribusi Penyewaan Sepeda per Jam (Line Chart) ----
st.subheader("⏰ Distribusi Penyewaan Sepeda per Jam")

# Menghitung jumlah penyewaan sepeda per jam
hourly_rentals = filtered_hour_df.groupby("hr")["cnt"].sum().reset_index()

# Visualisasi menggunakan line chart
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=hourly_rentals, marker="o", linestyle="-", color="b", ax=ax)

# Menambahkan label dan judul
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Distribusi Penyewaan Sepeda per Jam")

# Menampilkan semua jam dari 0-23
ax.set_xticks(range(0, 24))

# Menampilkan grid untuk meningkatkan keterbacaan
ax.grid(True)

# Menampilkan grafik
st.pyplot(fig)

# ---- MENAMPILKAN DATA ----
st.subheader("📋 Data Penyewaan Sepeda")
tab1, tab2 = st.tabs(["📅 Data Harian", "⏰ Data Per Jam"])

with tab1:
    st.write("Menampilkan 10 data pertama dari `clean_day.csv`:")
    st.dataframe(filtered_day_df.head(10))

with tab2:
    st.write("Menampilkan 10 data pertama dari `clean_hour.csv`:")
    st.dataframe(filtered_hour_df.head(10))