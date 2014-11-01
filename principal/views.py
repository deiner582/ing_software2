from django.shortcuts import render
from django.shortcuts import render_to_response
from transporte.models import *
# Create your views here.

def vista_index(request):

    return render_to_response('index.html',locals())

def vista_buses(request):
    return render_to_response('buses.html')

def vista_conductores(request):
    cond=conductor.objects.all()
    return  render_to_response('conductores.html',locals())

def vista_registro(request):
    return render_to_response('registro.html')

#Prueba de github proyeto de ing de software
#Prueba de github proyeto de ing de software
#Prueba de github proyeto de ing de software
#Prueba de github proyeto de ing de software