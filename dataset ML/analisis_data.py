# ==========================================
# 1. IMPORT LIBRARY
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 2. DATA LOADING
# ==========================================
df = pd.read_csv("StudentsPerformance.csv")

print("=== DATA LOADING ===")
print("Data berhasil dibaca!")
print("Jumlah baris dan kolom:", df.shape)
print("\n5 data pertama:")
print(df.head())

# ==========================================
# 3. DATA UNDERSTANDING
# ==========================================
print("\n=== DATA UNDERSTANDING ===")
print("\nInformasi dataset:")
df.info()

print("\nStatistik deskriptif:")
print(df.describe(include="all"))

print("\nNama kolom:")
print(df.columns.tolist())

# ==========================================
# 4. DATA CLEANING
# ==========================================
print("\n=== DATA CLEANING ===")

# Memeriksa data kosong
print("\nData kosong sebelum cleaning:")
print(df.isnull().sum())

# Memeriksa data duplikat
print("\nJumlah data duplikat:")
print(df.duplicated().sum())

# Menghapus data duplikat
df = df.drop_duplicates().copy()

# Menghapus spasi pada nama kolom
df.columns = df.columns.str.strip()

# Membersihkan spasi pada kolom teks
for kolom in df.select_dtypes(include="object").columns:
    df[kolom] = df[kolom].str.strip()

# Mengisi data kosong:
# numerik dengan median, teks dengan modus
for kolom in df.columns:
    if df[kolom].isnull().any():
        if pd.api.types.is_numeric_dtype(df[kolom]):
            df[kolom] = df[kolom].fillna(df[kolom].median())
        else:
            modus = df[kolom].mode()
            if not modus.empty:
                df[kolom] = df[kolom].fillna(modus[0])

print("\nData kosong setelah cleaning:")
print(df.isnull().sum())

print("\nUkuran data setelah cleaning:", df.shape)

# ==========================================
# 5. DATA ANALYSIS
# ==========================================
print("\n=== DATA ANALYSIS ===")

kolom_nilai = [
    "math score",
    "reading score",
    "writing score"
]

print("\nRata-rata nilai siswa:")
print(df[kolom_nilai].mean())

print("\nNilai tertinggi:")
print(df[kolom_nilai].max())

print("\nNilai terendah:")
print(df[kolom_nilai].min())

print("\nRata-rata nilai berdasarkan gender:")
print(df.groupby("gender")[kolom_nilai].mean())

# ==========================================
# 6. VISUALISASI DATA
# ==========================================
df[kolom_nilai].mean().plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Rata-rata Nilai Siswa")
plt.xlabel("Jenis Nilai")
plt.ylabel("Rata-rata")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Distribusi nilai matematika
plt.figure(figsize=(8, 5))
sns.histplot(df["math score"], bins=15, kde=True)
plt.title("Distribusi Nilai Matematika")
plt.xlabel("Nilai Matematika")
plt.ylabel("Jumlah Siswa")
plt.tight_layout()
plt.show()

# ==========================================
# 7. MENYIMPAN DATA HASIL CLEANING
# ==========================================
df.to_csv("StudentsPerformance_Cleaned.csv", index=False)

print("\n=== SELESAI ===")
print("Data bersih disimpan sebagai StudentsPerformance_Cleaned.csv")