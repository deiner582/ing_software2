from django.db import models
from ckeditor.fields import RichTextField
import datetime
# Create your models here.
class Persona(models.Model):
    identificacion=models.IntegerField(max_length=20,primary_key=True)
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField (max_length=30)
    fecha_nacimiento=models.DateField()

    def __unicode__(self):
        return self.nombres

class Autobus(models.Model):
    placa=models.CharField(max_length=6,primary_key=True)
    marca=models.CharField(max_length=50)
    foto=models.ImageField(upload_to="estaticos/img/autobuses")
    peso=models.IntegerField()
    consumo=models.CharField(max_length=50)
    velocidad_max=models.FloatField(max_length=3)
    precio=models.FloatField()

    def __unicode__(self):
        return self.placa

class Control_mecanico(models.Model):
    codigo=models.CharField(max_length=20,primary_key=True)
    autobus_placa=models.ForeignKey(Autobus)
    descripcion_fallo=RichTextField()
    costo_reparacion=models.FloatField()
    fecha_reparacion=models.DateField(auto_now=True)
    def __unicode__(self):
        return self.codigo

class Revisiones_Bus(models.Model):
    codigo_revision = models.CharField(max_length=20,primary_key=True)
    autobus_placa=models.ForeignKey(Autobus)
    descripcion_revision=RichTextField()
    fecha_revision=models.DateField(auto_now=True)
    def __unicode__(self):
        return self.codigo_revision

class Conductor(Persona):
    foto=models.ImageField(upload_to="estaticos/img/conductor")
    descripcion=RichTextField()
    autobus_placa=models.ForeignKey(Autobus)
    limite_hora_dia=models.IntegerField()
    limite_hora_semana=models.IntegerField()
    sueldo=models.IntegerField()
    def __unicode__(self):
        return (self.nombres + " "+ self.apellidos)

class Historia_Conductor(models.Model):
    codigo_ausencia=models.TextField(max_length=20,primary_key=True)
    conductor=models.ForeignKey(Conductor)
    fecha_ausencia=models.DateField()
    justificacion=RichTextField()
    def __unicode__(self):
        return self.codigo_ausencia

class Horas_Entrada_Salida(models.Model):
    codigo_horas=models.TextField(max_length=20,primary_key=True)
    conductor=models.ForeignKey(Conductor)
    hora_entrada=models.DateTimeField()
    hora_salida=models.DateTimeField()

class Paradas(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    ciudad=models.TextField(max_length=20)
    hora_salida=models.TimeField()
    hora_llegada=models.TimeField()

    def __unicode__(self):
        return (self.codigo+ " - "+ self.ciudad)

class Categoria(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    nombre=models.TextField(max_length=30)
    descripcion=models.TextField(max_length=100)
    costo=models.FloatField()

    def __unicode__(self):
        return self.nombre

class Trayecto(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    paradas_trayecto=models.ManyToManyField(Paradas)

    def __unicode__(self):
        return self.codigo

class Usuario(Persona):
    username=models.TextField()
    password=models.TextField()
    puntosAcumulados=models.IntegerField()

    def __unicode__(self):
        return (self.nombres +" "+ self.apellidos)

class Billetes(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    categoria=models.ForeignKey(Categoria)
    usuario=models.ForeignKey(Usuario)
    autobus=models.ForeignKey(Autobus)
    parada_origen=models.ForeignKey(Paradas,related_name="parada origen")
    parada_destino=models.ForeignKey(Paradas,related_name="parada destino")
    fecha_compra=models.DateTimeField()

    def __unicode__(self):
        return  self.codigo



