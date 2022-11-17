# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bandejatrabajo(models.Model):
    idot = models.BigIntegerField(primary_key=True)
    idreserva = models.BigIntegerField()
    rutempleado = models.BigIntegerField()
    descripcionot = models.CharField(max_length=50)
    totalot = models.BigIntegerField(blank=True, null=True)
    fechaot = models.DateField(blank=True, null=True)
    estadoot = models.BigIntegerField(blank=True, null=True)
    categoriaot = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bandejatrabajo'


class Cliente(models.Model):
    rutcliente = models.BigIntegerField(primary_key=True)
    dvcliente = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    rutempleado = models.BigIntegerField(primary_key=True)
    dvempleado = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'empleado'


class Facturacion(models.Model):
    nrodocumento = models.BigIntegerField(primary_key=True)
    tipodocumento = models.CharField(max_length=50)
    idot = models.BigIntegerField()
    ot_idot = models.BigIntegerField()
    ot_idreserva = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'facturacion'
        unique_together = (('nrodocumento', 'idot'), ('ot_idot', 'ot_idreserva'),)


class Ot(models.Model):
    idot = models.BigIntegerField(primary_key=True)
    idreserva = models.BigIntegerField()
    rutempleado = models.BigIntegerField()
    descripcionot = models.CharField(max_length=50)
    totalot = models.BigIntegerField()
    fechaot = models.DateField(blank=True, null=True)
    reserva_idreserva = models.BigIntegerField(unique=True)
    facturacion_nrodocumento = models.BigIntegerField()
    facturacion_idot = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ot'
        unique_together = (('idot', 'idreserva'), ('facturacion_nrodocumento', 'facturacion_idot'),)


class Productos(models.Model):
    idproducto = models.BigIntegerField(primary_key=True)
    nombreproducto = models.CharField(max_length=50)
    cantidad = models.BigIntegerField()
    tipoproducto = models.CharField(max_length=50)
    marcaproducto = models.CharField(max_length=50)
    idvehiculo = models.BigIntegerField()
    valorproducto = models.BigIntegerField()
    rutproveedor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedor(models.Model):
    rutproveedor = models.BigIntegerField(primary_key=True)
    dvproveedor = models.CharField(max_length=1)
    nombreproveedor = models.CharField(max_length=50)
    direccionproveedor = models.CharField(max_length=50)
    telefonocontacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Reserva(models.Model):
    idreserva = models.BigIntegerField(primary_key=True)
    rutcliente = models.BigIntegerField()
    idservicio = models.BigIntegerField()
    fechareserva = models.DateField()
    horareserva = models.DateField()
    canal = models.CharField(max_length=50)
    patente = models.CharField(max_length=50)
    idvehiculo = models.BigIntegerField()
    ot_idot = models.BigIntegerField()
    ot_idreserva = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'reserva'
        unique_together = (('ot_idot', 'ot_idreserva'),)


class Servicio(models.Model):
    idservicio = models.BigIntegerField(primary_key=True)
    tiposervicio = models.CharField(max_length=50)
    descservicio = models.CharField(max_length=50)
    valorservicio = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class Usuario(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    clave = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculos(models.Model):
    idvehiculo = models.BigIntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.BigIntegerField()
    tipovehiculo = models.CharField(max_length=50)
    cilindrada = models.BigIntegerField(blank=True, null=True)
    vin = models.CharField(max_length=50)
    reserva_idreserva = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculos'
