from django.contrib import admin

# Register your models here.
from .models import Categorias, Hoteles, TipoHabitacion, Habitaciones, Arduinos, Reserva, Cliente

admin.site.register(Categorias)
admin.site.register(Hoteles)
admin.site.register(TipoHabitacion)
admin.site.register(Habitaciones)
admin.site.register(Arduinos)
admin.site.register(Reserva)
admin.site.register(Cliente)