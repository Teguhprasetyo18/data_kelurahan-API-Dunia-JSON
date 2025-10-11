from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView 
from .models import  Warga, Pengaduan
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import WargaSerializer

# Create your views here.
class WargaListView(ListView):
    model = Warga
class WargaDetailView(DetailView):
    model = Warga
class PengaduanListView(ListView):
    model = Pengaduan
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Kita pakai template yang sama
    success_url = reverse_lazy('warga-list')
class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')
class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/Pengaduan_form.html'
    success_url = reverse_lazy('Pengaduan-list')
class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/Pengaduan_confirm_delete.html'
    success_url = reverse_lazy('Pengaduan-list')
class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


