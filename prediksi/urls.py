from django.urls import path  # Mengatur alamat URL
from . import views  # Mengambil fungsi dari views.py

urlpatterns = [
    path("", views.index, name="index"),  # Mengarahkan URL ke halaman prediksi
    path("evaluasi/", views.evaluasi, name="evaluasi"),  # Halaman evaluasi
]