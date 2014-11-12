from django.test import TestCase
from .models import *
# Create your tests here.
class Probar_bus(TestCase):
  def bus(self):
     Autobus.objects.create(placa='123',marca ="mazda",foto ="/c/c.jpj",peso = 180,  consumo = "1km por hora",  velocidad_max = 200,  precio = 200, puesto_bus =2)