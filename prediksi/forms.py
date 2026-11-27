from django import forms  # Mengambil library form Django

class CustomerForm(forms.Form):  # Membuat form input pelanggan
    Fresh = forms.IntegerField(label="Produk segar", min_value=0)  # Input produk segar
    Milk = forms.IntegerField(label="Produk susu", min_value=0)  # Input produk susu
    Grocery = forms.IntegerField(label="Kebutuhan sehari-hari", min_value=0)  # Input grocery
    Detergents_Paper = forms.IntegerField(label="Deterjen dan kertas", min_value=0)  # Input deterjen