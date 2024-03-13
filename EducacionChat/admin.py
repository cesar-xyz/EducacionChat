from django.contrib import admin

from .models import Empresa, Sucursal, Modulo, Trabajador, Sesion, Mensaje


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa']


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['nombre_sucursal', 'empresa', 'direccion']


@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ['modulo_id', 'nombre_modulo']


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    nombre_empresa = lambda self, obj: obj.sucursal.empresa.nombre_empresa
    nombre_empresa.short_description = 'Nombre Empresa'
    list_display = ['nomina', 'nombre_completo', 'nombre_empresa', 'puesto', 'sucursal']
    list_filter = ['sucursal']


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ['sesion_id', 'nomina']
    list_filter = ['nomina']


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ['mensaje_id', 'tiempo', 'pregunta', 'respuesta', 'sesion']
    list_filter = ['sesion']
