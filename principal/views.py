from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
import datetime
from transporte.models import *
from forms import *

# Create your views here.

def vista_index(request):
    if not request.user.is_anonymous():
        usuario = request.user
        iniciado = True
    else:
        iniciado = False
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def vista_buses(request):
    buses=Autobus.objects.all()
    return render_to_response('buses.html',locals())

def vista_conductores(request):
    cond=Conductor.objects.all()
    return  render_to_response('conductores.html',locals())

def vista_conductor_id(request,id_cond):
    cond=Conductor.objects.get(identificacion=id_cond)
    registro_entrada_salida=HoraEntradaSalida.objects.filter(conductor=id_cond)
    historial=HistorialConductor.objects.filter(conductor=id_cond)
    return render_to_response('condutor_detalle.html',locals(),context_instance=RequestContext(request))

def vista_bus_placa(request,p):
    bus=Autobus.objects.get(placa=p)
    fallosMecanicos = ControlMecanico.objects.filter(autobus_placa=p)
    revisiones = RevisionBus.objects.filter(autobus_placa=p)
    return render_to_response('bus_detalle.html',locals(),context_instance=RequestContext(request))

def comprar_viaje(request, cat):
    viaje=Viaje.objects.filter(categoria=cat)
    return render_to_response('comprar_viaje.html',locals(),context_instance=RequestContext(request))

def vista_registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
        return render_to_response('registro.html',locals(),context_instance=RequestContext(request))

def vista_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid():
            username = request.POST['username']
            clave = request.POST['password']
            acceso  = authenticate(username = username, password = clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    error = "login"
                    return render_to_response('login.html', locals())
                else:
                    error = "Error en el login"
                    return render_to_response('login.html', locals())
            else:
                error = "Error en el acceso"
                return render_to_response('login.html', locals())
    else:
        formulario = AuthenticationForm()
        
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))


def vista_billetes(request):
    categoria=Categoria.objects.all()
    return render_to_response('billetes.html',locals())
