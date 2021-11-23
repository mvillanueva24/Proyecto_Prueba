from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('categorias/', views.categorias),
    path('hoteles/', views.hoteles),
    path('tipohabitacion/', views.tipohabitacion),
    path('habitaciones/', views.habitaciones),
    path('arduinos/', views.arduinos),
    path('cliente/', views.cliente),
    path('reserva/', views.reserva),
    
]