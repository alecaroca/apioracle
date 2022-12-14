# Generated by Django 4.1.2 on 2022-11-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bandejatrabajo',
            fields=[
                ('idot', models.BigIntegerField(primary_key=True, serialize=False)),
                ('idreserva', models.BigIntegerField()),
                ('rutempleado', models.BigIntegerField()),
                ('descripcionot', models.CharField(max_length=50)),
                ('totalot', models.BigIntegerField(blank=True, null=True)),
                ('fechaot', models.DateField(blank=True, null=True)),
                ('estadoot', models.BigIntegerField(blank=True, null=True)),
                ('categoriaot', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bandejatrabajo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rutcliente', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dvcliente', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rutempleado', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dvempleado', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('nrodocumento', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipodocumento', models.CharField(max_length=50)),
                ('idot', models.BigIntegerField()),
                ('ot_idot', models.BigIntegerField()),
                ('ot_idreserva', models.BigIntegerField()),
            ],
            options={
                'db_table': 'facturacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ot',
            fields=[
                ('idot', models.BigIntegerField(primary_key=True, serialize=False)),
                ('idreserva', models.BigIntegerField()),
                ('rutempleado', models.BigIntegerField()),
                ('descripcionot', models.CharField(max_length=50)),
                ('totalot', models.BigIntegerField()),
                ('fechaot', models.DateField(blank=True, null=True)),
                ('reserva_idreserva', models.BigIntegerField(unique=True)),
                ('facturacion_nrodocumento', models.BigIntegerField()),
                ('facturacion_idot', models.BigIntegerField()),
            ],
            options={
                'db_table': 'ot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idproducto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombreproducto', models.CharField(max_length=50)),
                ('cantidad', models.BigIntegerField()),
                ('tipoproducto', models.CharField(max_length=50)),
                ('marcaproducto', models.CharField(max_length=50)),
                ('idvehiculo', models.BigIntegerField()),
                ('valorproducto', models.BigIntegerField()),
                ('rutproveedor', models.BigIntegerField()),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rutproveedor', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dvproveedor', models.CharField(max_length=1)),
                ('nombreproveedor', models.CharField(max_length=50)),
                ('direccionproveedor', models.CharField(max_length=50)),
                ('telefonocontacto', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idreserva', models.BigIntegerField(primary_key=True, serialize=False)),
                ('rutcliente', models.BigIntegerField()),
                ('idservicio', models.BigIntegerField()),
                ('fechareserva', models.DateField()),
                ('horareserva', models.DateField()),
                ('canal', models.CharField(max_length=50)),
                ('patente', models.CharField(max_length=50)),
                ('idvehiculo', models.BigIntegerField()),
                ('ot_idot', models.BigIntegerField()),
                ('ot_idreserva', models.BigIntegerField()),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idservicio', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tiposervicio', models.CharField(max_length=50)),
                ('descservicio', models.CharField(max_length=50)),
                ('valorservicio', models.BigIntegerField()),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.BigIntegerField(primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('idvehiculo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.BigIntegerField()),
                ('tipovehiculo', models.CharField(max_length=50)),
                ('cilindrada', models.BigIntegerField(blank=True, null=True)),
                ('vin', models.CharField(max_length=50)),
                ('reserva_idreserva', models.BigIntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'vehiculos',
                'managed': False,
            },
        ),
    ]
