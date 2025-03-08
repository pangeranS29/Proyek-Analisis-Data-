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
import pandas as pd  # Manipulasi data
import numpy as np  # Operasi numerik
import seaborn as sns  # Visualisasi data
import matplotlib.pyplot as plt  # Grafik dan plotting

# Analisis Statistik
from scipy import stats

# Analisis Geospasial
import geopandas as gpd
import folium
from streamlit_folium import folium_static
