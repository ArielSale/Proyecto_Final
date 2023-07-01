from django.shortcuts import render
from django.conf import settings
from carro.carro import Carro



# Vistas para secciones sin interacción del usuario

from django.shortcuts import render

def index(request):
    carro=Carro(request)
    return render(request, 'UmamiGastroApp/index.html')

def about(request):
    return render(request, 'UmamiGastroApp/about.html')

def products(request):
    return render(request, 'UmamiGastroApp/products.html')

def horarios(request):
    return render(request, 'UmamiGastroApp/horarios.html')


