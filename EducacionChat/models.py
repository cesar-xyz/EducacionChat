from django.db import models


class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=255, null=False)
    sucursal_matriz = models.ForeignKey('Sucursal', on_delete=models.CASCADE, related_name='matriz', null=True,
                                        blank=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['empresa_id']


class Sucursal(models.Model):
    sucursal_id = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=255, null=False)
    direccion = models.CharField(max_length=255, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='sucursales')

    def __str__(self):
        return self.nombre_sucursal + ' - ' + self.empresa.nombre_empresa

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['sucursal_id']


class Modulo(models.Model):
    modulo_id = models.IntegerField(primary_key=True)
    nombre_modulo = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nombre_modulo

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'
        ordering = ['modulo_id']


class Trabajador(models.Model):
    nomina = models.CharField(max_length=255, primary_key=True)
    nombre_completo = models.CharField(max_length=255, null=False)
    puesto = models.CharField(max_length=255, null=False)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='trabajadores')
    fecha_nacimiento = models.DateField(null=False)
    estado_civil = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=255, null=False)
    direccion_vivienda = models.CharField(max_length=255, null=False)
    salario = models.FloatField(null=True)
    fecha_ingreso_empresa = models.DateField(null=False)
    fecha_contratacion_puesto_actual = models.DateField(blank=True, null=True)
    turno_trabajo = models.CharField(max_length=255, null=False)
    condiciones_medicas = models.CharField(max_length=255, blank=True, null=True)
    conectividad = models.CharField(max_length=255, null=False)
    dispositivos_en_casa = models.IntegerField(null=False)
    escolaridad = models.CharField(max_length=255, null=False)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='trabajadores')

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['nomina']


class Sesion(models.Model):
    sesion_id = models.CharField(max_length=255, primary_key=True)
    nomina = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='sesiones')

    def __str__(self):
        return str(self.sesion_id)

    class Meta:
        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'
        ordering = ['sesion_id']


class Mensaje(models.Model):
    mensaje_id = models.AutoField(primary_key=True)
    tiempo = models.DateTimeField(null=False)
    pregunta = models.TextField(null=False)
    respuesta = models.TextField(null=False)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, related_name='mensajes')

    def __str__(self):
        return str(Sesion.objects.get(sesion_id=self.sesion_id).nomina)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['tiempo']
