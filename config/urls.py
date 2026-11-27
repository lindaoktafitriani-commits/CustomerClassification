from django.contrib import admin  # Mengakses fitur admin
from django.urls import path, include  # Mengatur routing website

urlpatterns = [
    path("admin/", admin.site.urls),  # Routing halaman admin
    path("", include("prediksi.urls")),  # Routing halaman prediksi
]