from django.db import models

# Create your models here.
class persona(models.Model):
    identificacion=models.IntegerField(max_length=20,primary_key=True)
    nombres=models.TextField(max_length=30)
    apellidos=models.TextField(max_length=30)
    fecha_nacimiento=models.DateField()

    def __unicode__(self):
        return self.nombres

class autobus(models.Model):
    placa=models.TextField(max_length=6,primary_key=True)
    marca=models.TextField(max_length=50)
    peso=models.FloatField()
    velocidad_max=models.FloatField(max_length=3)

    def __unicode__(self):
        return self.placa



class control_mecanico(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    autobus_placa=models.ForeignKey(autobus)
    descripcion_fallo=models.TextField(max_length=20)
    costo_reparacion=models.FloatField()

    def __unicode__(self):
        return self.codigo


class conductor(persona):
    autobus_placa=models.ForeignKey(autobus)
    limite_hora_dia=models.IntegerField(max_length=2)
    limite_hora_semana=models.IntegerField(max_length=3)
    sueldo=models.FloatField()

    def __unicode__(self):
        return self.nombres


class paradas(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    hora_salida=models.TimeField()
    hora_llegada=models.TimeField()

    def __unicode__(self):
        return self.codigo


class categoria(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    nombre=models.TextField(max_length=30)
    costo=models.FloatField()

    def __unicode__(self):
        return self.codigo

class trayecto(models.Model):
    codigo=models.TextField(max_length=20,primary_key=True)
    cod_categoria=models.ForeignKey(categoria)
    paradas_trayecto=models.ManyToManyField(paradas)

    def __unicode__(self):
        return self.codigo

class usuario(persona):
    puntosAcumulados=models.IntegerField()

    def __unicode__(self):
        return self.nombres


