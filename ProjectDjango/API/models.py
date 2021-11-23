from django.db import models
from django.db.models.base import Model
from django import forms

# Create your models here.
# ESTOY MODIFICANDO CON EL GIT.CESAR


class Categorias(models.Model):
    Nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre_categoria

class Hoteles(models.Model):
    Categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name="categoria_hoteles")
    Nombre_hotel = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=100)
    Calificacion = models.DecimalField(max_digits=1, decimal_places=0, name="Calificacion")
    Imagen = models.ImageField(upload_to='hoteles', blank=True,null=True)

    def __str__(self):
        return self.Categoria.Nombre_categoria + " - " + self.Nombre_hotel

class TipoHabitacion(models.Model):
    Tipo_habitacion = models.CharField(max_length=100)
    Cantidad_camas = models.DecimalField(max_digits=1, decimal_places=0)
    Precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.Tipo_habitacion

class Habitaciones(models.Model):

    ChoicesWifi = (
        ("1", "4G"),
        ("2", "5G")
    )

    ChoicesEstado = (
        ("1", "Disponible"),
        ("2", "No Disponible")
    )

    Nro_habitacion = models.CharField(max_length=3,default='')
    Hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE, related_name="hotel_habitaciones")
    Tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, related_name="tipo_habitacion_habitaciones")
    Imagen = models.ImageField(upload_to='habitaciones', blank=True, null=True)
    Estado_habitacion = models.CharField(max_length=2, choices=ChoicesEstado) # A  X  A="Habilitado"  X="Deshabilitado"
    Cerradura_electronica = models.BooleanField(default=True)
    Wifi = models.CharField(max_length=2, choices=ChoicesWifi) # 4G o 5G

    def __str__(self):
        return self.Hotel.Nombre_hotel + " - " + self.Nro_habitacion
    
## MODEL SENSORES ARDUINO
class Arduinos(models.Model):
    Habitacion = models.OneToOneField(Habitaciones, on_delete=models.CASCADE, related_name="habitacion_arduinos",default='')
    Arduino = models.CharField(max_length=100)
    Temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    Estado_ventalidor = models.BooleanField(default=True)
    Estado_calefactor = models.BooleanField(default=True)

    def __str__(self):
        return self.Arduino

class Cliente(models.Model):
    Nombre = models.CharField(max_length=100)
    Password = models.CharField(max_length=15)
    Correo = models.EmailField(max_length=100)
    def __str__(self):
        return self.Nombre

class Reserva(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cliente_reserva")
    Habitacion = models.ForeignKey(Habitaciones, on_delete=models.CASCADE, related_name="habitacion_reserva",default='')
    Fecha_inicio = models.DateField(auto_now=False)
    Fecha_fin = models.DateField(auto_now=False)
    Precio_total = models.DecimalField(max_digits=5, decimal_places=2)
    Token = models.CharField(max_length=100)

    def __str__(self):
        return self.Cliente.Nombre + " - " + self.Habitacion.Nro_habitacion