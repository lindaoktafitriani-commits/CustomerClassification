# Customer Type Predictor

Klasifikasi Jenis Pelanggan Distributor Berdasarkan Pola Pembelian Menggunakan Algoritma Decision Tree Berbasis Django.

**Identitas Mahasiswa**

Nama: Linda Oktavia Fitriani

NIM: 253307064

Kelas: 3C

Mata Kuliah: Sistem Cerdas

## Link Aplikasi

Website telah berhasil dideploy menggunakan PythonAnywhere
dan dapat diakses secara publik.

- [Prediksi Pelanggan](https://fitriani.pythonanywhere.com/)
- [Evaluasi Model](https://fitriani.pythonanywhere.com/evaluasi/)
  
## 1. Masalah yang Diselesaikan

Aplikasi ini bertujuan mengklasifikasikan jenis pelanggan distributor menjadi HoReCa (Hotel, Restoran, dan Kafe) atau Retail (pedagang eceran) berdasarkan pola pengeluaran tahunan pelanggan menggunakan machine learning.

## 2. Dataset

- Nama: Wholesale Customers Dataset
- Sumber: UCI Machine Learning Repository
- URL: https://archive.ics.uci.edu/dataset/292/wholesale+customers
- Lisensi: CC BY 4.0
- Jumlah data: 440 pelanggan
- Jumlah kolom: 8
- Distribusi kelas: 298 HoReCa dan 142 Retail
- Missing value: 0
- Data duplikat: 0

Fitur yang digunakan adalah Fresh, Milk, Grocery, dan Detergents_Paper. Target klasifikasi adalah Channel.

## 3. Metode

Teknik yang digunakan adalah machine learning dengan pendekatan supervised learning dan algoritma Decision Tree Classifier.

Dataset dibagi menjadi 75% data latih (330 data) dan 25% data uji (110 data). Model menggunakan criterion Gini, max_depth=3, dan random_state=42.

Model disimpan menggunakan Joblib dan diintegrasikan dengan framework Django untuk melakukan prediksi melalui website.

## 4. Hasil dan Evaluasi

| Metrik | Hasil |
|---|---:|
| Akurasi training | 94,24% |
| Akurasi testing | 95,45% |
| Precision (macro avg) | 94% |
| Recall (macro avg) | 95% |
| F1-score (macro avg) | 95% |
| Prediksi benar | 105 |
| Prediksi salah | 5 |

Berdasarkan hasil evaluasi, model mampu mengklasifikasikan 105 dari 110 data uji dengan benar.

Selisih akurasi training dan testing sebesar 1,21 poin persentase menunjukkan bahwa tidak terdapat indikasi overfitting yang kuat pada pembagian data tersebut.

## 5. Cara Menjalankan

Buka folder proyek menggunakan VS Code, kemudian jalankan perintah berikut pada terminal PowerShell.

```powershell
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python train_model.py
python manage.py migrate
python manage.py runserver
```

Buka website melalui http://127.0.0.1:8000/.

Halaman prediksi digunakan untuk mengklasifikasikan pelanggan, sedangkan halaman evaluasi menampilkan hasil pengujian model, confusion matrix, dan visualisasi Decision Tree.

## 6. Refleksi Singkat

Proyek ini berhasil mengimplementasikan algoritma Decision Tree untuk klasifikasi jenis pelanggan dan mengintegrasikannya dengan framework Django.

Keterbatasan model adalah jumlah dataset yang relatif kecil, distribusi kelas yang tidak seimbang, serta penggunaan empat fitur pengeluaran. Hasil evaluasi belum menjamin performa yang sama pada pelanggan distributor lain.

Pengembangan selanjutnya dapat dilakukan dengan menambah data dan fitur serta melakukan validasi silang untuk menguji kestabilan model.

## 7. Referensi

- Modul 9 — Pengantar Machine Learning.
- Modul 10 — Evaluasi Model dan Data Nyata.
- Buku Ajar Bab 7 — Machine Learning.
- Modul 15 — UAS Demo Proyek Akhir.
- Cardoso, M. (2013). Wholesale Customers. UCI Machine Learning Repository. https://doi.org/10.24432/C5030X.
