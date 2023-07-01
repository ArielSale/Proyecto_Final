from django.urls import path
from . import views

app_name = 'Contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('valido/', views.contact_valido, name='contact_valido'), # Ruta para el redirect con el parámetro valido
    path('no_valido/', views.contact_no_valido, name='contact_no_valido'), # Ruta para el redirect con el parámetro no_valido
]