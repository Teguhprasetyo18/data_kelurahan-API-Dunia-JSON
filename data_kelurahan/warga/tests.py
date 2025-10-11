from django.test import TestCase
from django import forms
from .models import Warga, Pengaduan

# Create your tests here.
class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['warga', 'isi_pengaduan', 'tanggal_pengaduan']