from django.urls import path, include
from .views import BandejatrabajoViewset, ClienteViewset,EmpleadoViewset,FacturacionViewset,OtViewset,ProductosViewset,ProveedorViewset,ReservaViewset,ServicioViewset,VehiculosViewset,UsuarioViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('bandejatrabajo', BandejatrabajoViewset)
router.register('Cliente', ClienteViewset)
router.register('Empleado', EmpleadoViewset)
router.register('facturacion', FacturacionViewset)
router.register('ot', OtViewset)
router.register('productos', ProductosViewset)
router.register('proveedor', ProveedorViewset)
router.register('reserva', ReservaViewset)
router.register('servicio', ServicioViewset)
router.register('vehiculos', VehiculosViewset)
router.register('Usuario', UsuarioViewset)


urlpatterns = [
    
    path('', include(router.urls)),
]
