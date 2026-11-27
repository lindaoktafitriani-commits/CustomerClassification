
import pandas as pd  # Mengolah data input pengguna
import joblib  # Memuat model Decision Tree
import json  # Membaca hasil evaluasi

from django.shortcuts import render  # Menampilkan halaman HTML
from django.conf import settings  # Mengakses konfigurasi Django
from .forms import CustomerForm  # Mengambil form pelanggan

model = joblib.load(settings.BASE_DIR / "model_decision_tree.pkl")  # Memuat model


# HALAMAN PREDIKSI
def index(request):  # Fungsi halaman utama

    hasil = None  # Menyiapkan hasil prediksi
    form = CustomerForm()  # Membuat form kosong

    if request.method == "POST":  # Memeriksa pengiriman form

        form = CustomerForm(request.POST)  # Mengambil input pengguna

        if form.is_valid():  # Memvalidasi input

            data_baru = pd.DataFrame(
                [form.cleaned_data],  # Mengambil input yang valid
                columns=model.feature_names_in_  # Menyesuaikan urutan fitur
            )

            hasil = model.predict(data_baru)[0]  # Melakukan klasifikasi

    return render(request, "prediksi/index.html", {
        "form": form,  # Mengirim form ke HTML
        "hasil": hasil  # Mengirim hasil prediksi
    })


# HALAMAN EVALUASI
def evaluasi(request):  # Fungsi halaman evaluasi

    with open(settings.BASE_DIR / "evaluasi.json", "r") as file:  # Membuka JSON
        data = json.load(file)  # Membaca hasil evaluasi

    return render(request, "prediksi/evaluasi.html", data)  # Menampilkan evaluasi
