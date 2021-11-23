from rest_framework import serializers

from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
    
class HotelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoteles
        fields = '__all__'

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'
    
class HabitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitaciones
        fields = '__all__'

class ArduinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arduinos
        fields = '__all__'
    
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'