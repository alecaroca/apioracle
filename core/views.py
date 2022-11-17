from django.shortcuts import render
from .models import Bandejatrabajo,Cliente,Empleado,Facturacion,Ot,Productos,Proveedor,Reserva,Servicio,Vehiculos, Usuario
from rest_framework import viewsets
from .serializers import BandejatrabajoSerializer, ClienteSerializer, EmpleadoSerializer, FacturacionSerializer, OtSerializer, ProductosSerializer, ProveedorSerializer, ReservaSerializer,ServicioSerializer, VehiculosSerializer, UsuarioSerializer
# Create your views here.

class BandejatrabajoViewset(viewsets.ModelViewSet):
    queryset = Bandejatrabajo.objects.all()
    serializer_class = BandejatrabajoSerializer

    def get_queryset(self):
        bandejatrabajo = Bandejatrabajo.objects.all()
        rutempleado =self.request.GET.get('rutempleado')
        if rutempleado:
            bandejatrabajo= bandejatrabajo.filter(rutempleado=rutempleado)
        return bandejatrabajo
        
    

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer      

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class FacturacionViewset(viewsets.ModelViewSet):
    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

class OtViewset(viewsets.ModelViewSet):
    queryset = Ot.objects.all()
    serializer_class = OtSerializer

class ProductosViewset(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ProveedorViewset(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ReservaViewset(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def get_queryset(self):
        reserva = Reserva.objects.all()
        rutcliente =self.request.GET.get('rutcliente')
        if rutcliente:
            reserva= reserva.filter(rutcliente=rutcliente)
        return reserva   

class ServicioViewset(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class VehiculosViewset(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculosSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer