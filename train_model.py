
import pandas as pd  # Mengolah dataset
import matplotlib.pyplot as plt  # Membuat grafik
import joblib  # Menyimpan model
from pathlib import Path  # Mengatur lokasi file

from sklearn.model_selection import train_test_split  # Membagi data
from sklearn.tree import DecisionTreeClassifier, plot_tree  # Decision Tree
from sklearn.metrics import classification_report, ConfusionMatrixDisplay  # Evaluasi

# 1. Membaca dataset
BASE_DIR = Path(__file__).resolve().parent  # Menentukan folder utama proyek
df = pd.read_csv("https://raw.githubusercontent.com/lindaoktafitriani-commits/SISTEM_CERDAS/refs/heads/main/Wholesale%20customers%20data.csv")  # Membaca CSV
print(df.head())  # Menampilkan lima data pertama

# 2. Eksplorasi dan preprocessing
print("Ukuran data:", df.shape)  # Jumlah baris dan kolom
df.info()  # Informasi struktur dataset
print("Data kosong:\n", df.isnull().sum())  # Memeriksa missing value
print("Duplikat:", df.duplicated().sum())  # Memeriksa duplikat

df = df.dropna().drop_duplicates()  # Membersihkan dataset
df["Channel"] = df["Channel"].map({1: "HoReCa", 2: "Retail"})  # Mengubah label
print(df["Channel"].value_counts())  # Distribusi kelas

# 3. Menentukan fitur dan target
fitur = ["Fresh", "Milk", "Grocery", "Detergents_Paper"]  # Empat fitur
X = df[fitur]  # Fitur masukan
y = df["Channel"]  # Target klasifikasi

# 4. Membagi data
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y,  # Fitur dan target
    test_size=0.25,  # 25% data uji
    random_state=42,  # Pembagian konsisten
    stratify=y  # Menjaga proporsi kelas
)

# 5. Training model
model = DecisionTreeClassifier(max_depth=3, random_state=42)  # Membuat model
model.fit(X_latih, y_latih)  # Melatih model
prediksi = model.predict(X_uji)  # Prediksi data uji

# 6. Evaluasi model
print("Akurasi latih:", model.score(X_latih, y_latih))  # Akurasi training
print("Akurasi uji:", model.score(X_uji, y_uji))  # Akurasi testing
print(classification_report(y_uji, prediksi, zero_division=0))  # Metrik evaluasi

# 7. Confusion matrix
ConfusionMatrixDisplay.from_predictions(y_uji, prediksi, cmap="Blues")  # Matriks
plt.title("Confusion Matrix")  # Judul grafik
plt.savefig(BASE_DIR / "confusion_matrix.png")  # Menyimpan gambar
plt.close()  # Menutup grafik

# 8. Visualisasi Decision Tree
plt.figure(figsize=(16, 8))  # Ukuran gambar
plot_tree(model, feature_names=fitur, class_names=model.classes_, filled=True)  # Pohon
plt.savefig(BASE_DIR / "decision_tree.png", bbox_inches="tight")  # Menyimpan pohon
plt.close()  # Menutup grafik

# 9. Menyimpan model
joblib.dump(model, BASE_DIR / "model_decision_tree.pkl")  # Menyimpan model
print("Training model berhasil!")  # Informasi keberhasilan

import json  # Library untuk menyimpan data evaluasi
import shutil  # Library untuk menyalin file

folder_static = BASE_DIR / "prediksi" / "static" / "prediksi"  # Lokasi gambar
folder_static.mkdir(parents=True, exist_ok=True)  # Membuat folder jika belum ada

shutil.copy2(BASE_DIR / "confusion_matrix.png", folder_static)  # Menyalin confusion matrix
shutil.copy2(BASE_DIR / "decision_tree.png", folder_static)  # Menyalin pohon keputusan

evaluasi = {  # Membuat dictionary hasil evaluasi
    "akurasi_latih": model.score(X_latih, y_latih) * 100,  # Persentase akurasi latih
    "akurasi_uji": model.score(X_uji, y_uji) * 100,  # Persentase akurasi uji
    "jumlah_latih": len(X_latih),  # Jumlah data training
    "jumlah_uji": len(X_uji),  # Jumlah data testing
    "laporan": classification_report(y_uji, prediksi, zero_division=0)  # Metrik evaluasi
}

with open(BASE_DIR / "evaluasi.json", "w") as file:  # Membuka file JSON
    json.dump(evaluasi, file, indent=4)  # Menyimpan hasil evaluasi