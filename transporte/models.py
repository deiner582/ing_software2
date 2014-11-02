from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Persona(models.Model):
    identificacion=models.IntegerField(max_length=20,primary_key=True)
    nombres=models.TextField(max_length=30)
    apellidos=models.TextField(max_length=30)
    fecha_nacimiento=models.DateField()

    def __unicode__(self):
        return self.nombres

class Autobus(models.Model):
    placa=models.TextField(max_length=6,primary_key=True)
    marca=models.TextField(max_length=50)
    peso=models.FloatField()
    velocidad_max=models.FloatField(max_length=3)
    precio=models.FloatField()
    def __unicode__(self):
        return self.placa



class Control_mecanico(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    autobus_placa=models.ForeignKey(Autobus)
    descripcion_fallo=RichTextField()
    costo_reparacion=models.FloatField()

    def __unicode__(self):
        return self.codigo


class Conductor(Persona):
    foto=RichTextField()
    descripcion=RichTextField()
    autobus_placa=models.ForeignKey(Autobus)
    limite_hora_dia=models.IntegerField(max_length=2)
    limite_hora_semana=models.IntegerField(max_length=3)
    sueldo=models.FloatField()

    def __unicode__(self):
        return self.nombres


class Paradas(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    hora_salida=models.TimeField()
    hora_llegada=models.TimeField()

    def __unicode__(self):
        return self.codigo


class Categoria(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    nombre=models.TextField(max_length=30)
    costo=models.FloatField()

    def __unicode__(self):
        return self.codigo

class Trayecto(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    cod_categoria=models.ForeignKey(Categoria)
    paradas_trayecto=models.ManyToManyField(Paradas)

    def __unicode__(self):
        return self.codigo

class Usuario(Persona):
    puntosAcumulados=models.IntegerField()

    def __unicode__(self):
        return self.nombres


