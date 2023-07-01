from django.shortcuts import render
from .models import Producto

def store(request):
    productos = Producto.objects.all()
    return render(request, 'Store/store.html', {'productos': productos})
