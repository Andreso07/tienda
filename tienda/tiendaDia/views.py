from django.http import HttpResponse
from django.shortcuts import render
from tiendaDia.models import Producto, Venta
from django.views.generic import ListView, DetailView 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def first_view(request):
    return render(request, 'base.html')

class ProductoListView(ListView):
    model = Producto
class ProductoDetailView(DetailView):
    model = Producto

class VentaListView(ListView):
    model = Venta
class VentaDetailView(DetailView):
    model = Venta

class VentaCreate(CreateView):
    model = Venta
    fields='__all__'
class ProductoCreate(CreateView):
    model = Producto
    fields='__all__'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')
class VentaDelete(DeleteView):
    model = Venta
    success_url = reverse_lazy('venta-list')


class ProductoUpdate(UpdateView):
    model = Producto
    fields='__all__'
class VentaUpdate(UpdateView):
    model = Venta
    fields='__all__'