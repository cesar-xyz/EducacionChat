# Generated by Django 4.1 on 2024-03-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducacionChat', '0008_alter_sesion_sesion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='pregunta',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='respuesta',
            field=models.TextField(),
        ),
    ]
