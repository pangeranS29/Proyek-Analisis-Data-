
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- GATHERING DATA ----
st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚲")



# Load dataset dengan metode yang diminta
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
- **4 (Musim Dingin ❄️)** 
""")


selected_weathersit = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    day_df["weathersit"].unique(),
    default=day_df["weathersit"].unique()
)

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

# ---- VISUALISASI 1: Pengaruh Cuaca terhadap Penyewaan Sepeda ----
st.subheader("☁️ Pengaruh Cuaca terhadap Penyewaan Sepeda (Harian)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="weathersit", y="cnt", data=filtered_day_df, ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda (Harian)")
st.pyplot(fig)

# ---- VISUALISASI 2: Waktu dengan Penyewaan Sepeda Terbanyak ----
st.subheader("⏰ Waktu dengan Jumlah Penyewaan Sepeda Terbanyak (Per Jam)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=filtered_hour_df, ci=None, ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Distribusi Penyewaan Sepeda per Jam")
st.pyplot(fig)

# ---- MENAMPILKAN DATA ----
st.subheader("📋 Data Penyewaan Sepeda")
tab1, tab2 = st.tabs(["📅 Data Harian", "⏰ Data Per Jam"])

with tab1:
    st.write("Menampilkan 10 data pertama dari `clean_day.csv`:")
    st.dataframe(day_df.head(10))

with tab2:
    st.write("Menampilkan 10 data pertama dari `clean_hour.csv`:")
    st.dataframe(hour_df.head(10))


# Jalankan dengan: streamlit run dashboard.py

