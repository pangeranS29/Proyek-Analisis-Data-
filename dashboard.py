import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Load dataset
all_df = pd.read_csv("clean_day.csv")
all_df['dteday'] = pd.to_datetime(all_df['dteday'])

# Sidebar
st.sidebar.header("Filter Data")
st.sidebar.markdown("### Keterangan Musim:")
st.sidebar.markdown("""
1️⃣ **Semi**  
2️⃣ **Panas**  
3️⃣ **Gugur**  
4️⃣ **Dingin**
""")

# Pilihan filter musim
season_options = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
selected_season = st.sidebar.multiselect("Pilih Musim:", list(season_options.keys()), default=list(season_options.keys()))

# Filter data
filtered_df = all_df[all_df['season'].isin(selected_season)]

# Judul Dashboard
st.title("📊 Dashboard Analisis Bike Sharing")

# Tampilkan Data
st.subheader("🔍 Data Bike Sharing")
st.dataframe(filtered_df.head())

# Statistik Deskriptif
st.subheader("📈 Statistik Deskriptif")
st.write(filtered_df.describe())

# Penyewaan Sepeda Berdasarkan Musim
st.subheader("🚴‍♂️ Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=filtered_df['season'].map(season_options), y=filtered_df['cnt'], estimator=sum, palette='coolwarm', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Total Penyewaan Sepeda per Musim")
st.pyplot(fig)

# Pengaruh Hari Kerja terhadap Penyewaan Sepeda
st.subheader("📅 Pengaruh Hari Kerja terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='workingday', y='cnt', data=filtered_df, palette="Set2", ax=ax)
ax.set_xlabel("Hari Kerja (0 = Tidak, 1 = Ya)")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Distribusi Penyewaan Sepeda pada Hari Kerja vs Libur")
st.pyplot(fig)

# Korelasi Antar Variabel
st.subheader("📌 Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
ax.set_title("Matriks Korelasi")
st.pyplot(fig)

# Insight dari Analisis Data
st.subheader("🔎 Insight dari Analisis Data")
st.markdown("""
- **Musim Gugur memiliki jumlah penyewaan sepeda tertinggi**, sedangkan **Musim Semi** memiliki jumlah penyewaan terendah.
- **Hari kerja memiliki jumlah penyewaan yang lebih tinggi dibandingkan hari libur**, menandakan banyak pengguna menggunakan sepeda untuk transportasi kerja.
- **Temperatur dan kelembapan memiliki pengaruh terhadap jumlah penyewaan sepeda**, suhu yang lebih tinggi cenderung meningkatkan jumlah penyewaan.
""")

# Jalankan dengan: streamlit run dashboard.py
