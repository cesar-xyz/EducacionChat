from rest_framework import generics

from .models import Mensaje, Sesion, Trabajador, Empresa, Modulo, Sucursal
from .serializers import MensajeSerializer, SesionSerializer, TrabajadorSerializer, EmpresaSerializer, ModuloSerializer, \
    SucursalSerializer


class MensajeCreateAPIView(generics.CreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class SesionCreateAPIView(generics.CreateAPIView):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer


class TrabajadorCreateAPIView(generics.CreateAPIView):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer


class EmpresaListAPIView(generics.ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class ModuloListAPIView(generics.ListAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class SucursalListAPIView(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
