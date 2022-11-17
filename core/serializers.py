from .models import Bandejatrabajo,Cliente,Empleado,Facturacion,Ot,Productos,Proveedor,Reserva,Servicio,Vehiculos, Usuario
from rest_framework import serializers

class BandejatrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandejatrabajo
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturacion
        fields = '__all__'

class OtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ot
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'