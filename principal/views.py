from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from transporte.models import *
from forms import *
# Create your views here.

def vista_index(request):

    return render_to_response('index.html',locals())

def vista_buses(request):
    return render_to_response('buses.html')

def vista_conductores(request):
    cond=Conductor.objects.all()
    return  render_to_response('conductores.html',locals())

def vista_registro(request):
    return render_to_response('registro.html')
<<<<<<< HEAD



=======
>>>>>>> f4bc4f6a7143e7ee55f3eaad9adad960198df53b
