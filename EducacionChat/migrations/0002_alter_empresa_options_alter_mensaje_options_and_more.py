# Generated by Django 4.1 on 2024-02-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducacionChat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['empresa_id'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='mensaje',
            options={'ordering': ['timestamp'], 'verbose_name': 'Mensaje', 'verbose_name_plural': 'Mensajes'},
        ),
        migrations.AlterModelOptions(
            name='modulo',
            options={'ordering': ['modulo_id'], 'verbose_name': 'Modulo', 'verbose_name_plural': 'Modulos'},
        ),
        migrations.AlterModelOptions(
            name='sesion',
            options={'ordering': ['sesion_id'], 'verbose_name': 'Sesion', 'verbose_name_plural': 'Sesiones'},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'ordering': ['sucursal_id'], 'verbose_name': 'Sucursal', 'verbose_name_plural': 'Sucursales'},
        ),
        migrations.AlterModelOptions(
            name='trabajador',
            options={'ordering': ['nomina'], 'verbose_name': 'Trabajador', 'verbose_name_plural': 'Trabajadores'},
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='modulo_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
