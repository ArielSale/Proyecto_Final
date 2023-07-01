from django.urls import path
from . import views

app_name = 'UmamiGastroApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('horarios/', views.horarios, name='horarios'),
]