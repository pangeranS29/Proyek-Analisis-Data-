# 🚲 Dashboard Analisis Penyewaan Sepeda

## 📖 1. Pendahuluan
Studi kasus ini bertujuan untuk menganalisis tren penyewaan sepeda dengan menggunakan dataset `day.csv`.  
Kami akan mengeksplorasi tren penggunaan sepeda berdasarkan faktor-faktor seperti **musim**, **cuaca**, **waktu**, dan **kondisi lingkungan**.

### 🎯 **Tujuan Analisis**
1. **Mengetahui pola penyewaan sepeda** berdasarkan waktu (harian, bulanan, dan musim).
2. **Menganalisis pengaruh faktor cuaca** terhadap jumlah penyewaan sepeda.
3. **Mengelompokkan pola pengguna** dengan teknik **RFM Analysis** dan **Clustering**.
4. **Melakukan analisis geospasial** (jika tersedia data lokasi penyewaan).

---

## 🔗 2. Import Library
Sebelum memulai analisis, kita perlu mengimpor semua library yang digunakan dalam proyek ini.

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## Run  : Streamlit run Dashboard.py