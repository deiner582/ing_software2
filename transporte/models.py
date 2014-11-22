from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import *
from datetime import date,datetime,time,timedelta

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
    peso = models.IntegerField(validators=[MinValueValidator(15000), MaxValueValidator(18000)])
    consumo = models.CharField(max_length=50)
    velocidad_max = models.IntegerField(validators=[MinValueValidator(000), MaxValueValidator(250)])
    precio = models.IntegerField(validators=[MinValueValidator(50000000), MaxValueValidator(200000000)])
    puesto_bus = models.IntegerField(validators=[MinValueValidator(26), MaxValueValidator(32)])

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
    
    def _horas_semanales(self):
        return self.limite_hora_dia * 5

    limite_hora_semana = property(_horas_semanales)

    def _sueldo_base(self):
        return self.limite_hora_semana * 4 * 25000

    sueldo = property(_sueldo_base)

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
    def _horas_trabajadas(self):
            return abs(self.hora_salida.hour - self.hora_entrada.hour)

    horas_trabajadas = property(_horas_trabajadas)

    def _horas_extras(self):
        return abs(self.horas_trabajadas - self.conductor.limite_hora_dia)
    horas_extras = property(_horas_extras)

    def __unicode__(self):
        return self.codigo

class Ciudad(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    ciudad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ciudad

class Trayecto(models.Model):
    codigo=models.CharField(max_length=5, primary_key=True)
    ciudad_origen = models.ForeignKey(Ciudad, related_name='Origen')
    ciudad_destino = models.ForeignKey(Ciudad, related_name='Destino')
    distancia_trayecto = models.IntegerField(max_length=5, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    tiempo_estimado = models.IntegerField(max_length=3, validators=[MinValueValidator(1), MaxValueValidator(999)])

    def __unicode__(self):
        return self.origen +" "+ self.destino

class Categoria(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    costo = models.IntegerField(max_length=6)

    def __unicode__(self):
        return self.nombre

class Horario(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    hora = models.TimeField()

class Viaje(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    bus_asignado = models.ForeignKey(Autobus)
    categoria = models.ForeignKey(Categoria)
    origen = models.ForeignKey(Ciudad, related_name="Origen Viaje")
    destino = models.ForeignKey(Ciudad, related_name="Destino Viaje")
    horario = models.ForeignKey(Horario)
    trayectos = models.ManyToManyField(Trayecto)
    tipo = models.CharField(max_length=12, choices=(('Ida', 'Ida'), ('Ida y vuelta', 'Ida y Vuelta')))

    def __unicode__(self):
        return self.codigo

class Billete(models.Model):
    codigo = models.TextField(max_length=5, primary_key=True)
    viaje = models.ForeignKey(Viaje)
    usuario = models.ForeignKey(User)
    fecha_viaje = models.DateField()

    def __unicode__(self):
        return  self.codigo