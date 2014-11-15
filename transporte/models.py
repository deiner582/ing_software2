from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import *
import datetime

# Create your models here.
class Persona(models.Model):
    identificacion = models.IntegerField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __unicode__(self):
        return self.nombres

class Autobus(models.Model):
    placa = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="estaticos/img/autobuses")
    peso = models.IntegerField(max_length=5)
    consumo = models.CharField(max_length=50)
    velocidad_max = models.IntegerField(validators=[MinValueValidator(000), MaxValueValidator(250)])
    precio = models.IntegerField(max_length=9)
    puesto_bus = models.IntegerField(max_length=2)

    def __unicode__(self):
        return self.placa

class ControlMecanico(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    autobus_placa = models.ForeignKey(Autobus)
    descripcion_fallo = RichTextField()
    costo_reparacion = models.FloatField()
    fecha_reparacion = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.codigo

class RevisionBus(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    autobus_placa = models.ForeignKey(Autobus)
    descripcion_revision = RichTextField()
    fecha_revision = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.codigo_revision

class Conductor(Persona):
    autobus_placa=models.ForeignKey(Autobus)
    foto = models.ImageField(upload_to="estaticos/img/conductor")
    descripcion = RichTextField()
    limite_hora_dia = models.IntegerField(max_length=2)
    limite_hora_semana = models.CharField(max_length=8, ) # Colocar Formato
    sueldo = models.IntegerField(max_length=7)

    def __unicode__(self):
        return (self.nombres + " "+ self.apellidos)

class HistorialConductor(models.Model):
    codigo_ausencia = models.CharField(max_length=5, primary_key=True)
    conductor = models.ForeignKey(Conductor)
    fecha_ausencia = models.DateField()
    justificacion=RichTextField()

    def __unicode__(self):
        return self.codigo_ausencia

class HoraEntradaSalida(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    conductor = models.ForeignKey(Conductor)
    fecha_entrada = models.DateField(null=True)
    hora_entrada = models.TimeField(null=True)
    fecha_salida = models.DateField(null=True)
    hora_salida = models.TimeField(null=True)

    def __unicode__(self):
        return self.codigo

class Ciudad(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    ciudad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ciudad

class Parada(models.Model):
    codigo=models.CharField(max_length=5, primary_key=True)
    ciudad = models.ForeignKey(Ciudad)
    hora_llegada = models.TimeField()
    hora_salida = models.TimeField()

    def __unicode__(self):
        return self.codigo

class Categoria(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    costo = models.IntegerField(max_length=6)

    def __unicode__(self):
        return self.nombre

class Usuario(Persona):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=16)
    puntosAcumulados = models.IntegerField(max_length=5)

    def __unicode__(self):
        return (self.nombres +" "+ self.apellidos)

class Horario(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    hora = models.TimeField()

class Viaje(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    bus_asignado = models.ForeignKey(Autobus)
    categoria = models.ForeignKey(Categoria)
    origen = models.ForeignKey(Parada, related_name="Origen")
    destino = models.ForeignKey(Parada, related_name="Destino")
    tipo = models.CharField(max_length=12, choices=(('Ida', 'Ida'), ('Ida y vuelta', 'Ida y Vuelta')))
    precio_base = models.IntegerField(max_length=5)
    precio_total = models.IntegerField(max_length=5)
    descuento = models.IntegerField(max_length=5, null=True)
    horario = models.ForeignKey(Horario)

    def __unicode__(self):
        return self.codigo

class Billete(models.Model):
    codigo = models.TextField(max_length=5, primary_key=True)
    viaje = models.ForeignKey(Viaje)
    usuario = models.ForeignKey(Usuario)
    fecha_viaje = models.DateField()

    def __unicode__(self):
        return  self.codigo