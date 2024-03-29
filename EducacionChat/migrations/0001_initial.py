# Generated by Django 4.1 on 2024-02-29 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresa_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('modulo_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_modulo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('sucursal_id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sucursales', to='EducacionChat.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('nomina', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_civil', models.CharField(blank=True, max_length=255, null=True)),
                ('genero', models.CharField(max_length=255)),
                ('direccion_vivienda', models.CharField(max_length=255)),
                ('salario', models.FloatField(null=True)),
                ('fecha_ingreso_empresa', models.DateField()),
                ('fecha_contratacion_puesto_actual', models.DateField(blank=True, null=True)),
                ('turno_trabajo', models.CharField(max_length=255)),
                ('condiciones_medicas', models.CharField(blank=True, max_length=255, null=True)),
                ('conectividad', models.CharField(max_length=255)),
                ('dispositivos_en_casa', models.CharField(max_length=255)),
                ('escolaridad', models.CharField(max_length=255)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='EducacionChat.modulo')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='EducacionChat.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('sesion_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nomina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesiones', to='EducacionChat.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('mensaje_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('pregunta', models.CharField(max_length=255)),
                ('respuesta', models.CharField(max_length=255)),
                ('sesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='EducacionChat.sesion')),
            ],
        ),
    ]
