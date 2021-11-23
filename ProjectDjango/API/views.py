from http.client import responses
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'mensaje': 'API RESTFULL PROYECTO FINAL'})

@api_view(['GET'])
def categorias(request):
    lista_categoria = Categorias.objects.all()
    serCategoria = CategoriaSerializer(lista_categoria,many=True)
    return Response(serCategoria.data)

@api_view(['GET'])
def hoteles(request):
    lista_hoteles = Hoteles.objects.all()
    serHoteles = HotelesSerializer(lista_hoteles,many=True)
    return Response(serHoteles.data)

@api_view(['GET'])
def tipohabitacion(request):
    lista_thabitacion = TipoHabitacion.objects.all()
    serthabitacion = TipoHabitacionSerializer(lista_thabitacion,many=True)
    return Response(serthabitacion.data)

@api_view(['GET'])
def habitaciones(request):
    lista_habitacion = Habitaciones.objects.all()
    serHabitacion = HabitacionesSerializer(lista_habitacion,many=True)
    return Response(serHabitacion.data)

@api_view(['GET'])
def arduinos(request):
    lista_arduinos = Arduinos.objects.all()
    serArduinos = ArduinosSerializer(lista_arduinos,many=True)
    return Response(serArduinos.data)

@api_view(['GET'])
def cliente(request):
    lista_cliente = Cliente.objects.all()
    serCliente = ClienteSerializer(lista_cliente,many=True)
    return Response(serCliente.data)

@api_view(['GET'])
def reserva(request):
    lista_habitacion = Reserva.objects.all()
    serReserva = ReservaSerializer(lista_habitacion,many=True)
    return Response(serReserva.data)

