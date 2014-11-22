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

def index(request):
    return render_to_response('base.html',locals(),context_instance=RequestContext(request))

def registrar(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FormularioRegistro()
    data = {'form': form,}
    return render_to_response('registrarse.html', data, context_instance=RequestContext(request))

def loguear(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = request.POST['usuario']
            password = request.POST['contrasena']
            resultado = "Formulario Valido"
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                     resultado = "Usuario no Logueado"
            else:
                 resultado = "Error de Usuario o Contrasena"
        else:
            resultado = "Formulario en los Datos del  Formulario"
    else:
        form = FormularioLogin()
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

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

    def _sueldo_total():
        sueldo_total = 0
        sum_horas_extras = 0
        for rea in registro_entrada_salida:
            sum_horas_extras = sum_horas_extras + rea.horas_extras
        sueldo_total = cond.sueldo + sum_horas_extras * 25000
        return sueldo_total
        
    sueldo_total = _sueldo_total
    return render_to_response('condutor_detalle.html',locals(),context_instance=RequestContext(request))

def vista_bus_placa(request,p):
    bus=Autobus.objects.get(placa=p)
    fallosMecanicos = ControlMecanico.objects.filter(autobus_placa=p)
    revisiones = RevisionBus.objects.filter(autobus_placa=p)
    return render_to_response('bus_detalle.html',locals(),context_instance=RequestContext(request))

def comprar_viaje(request, cat):
    viaje=Viaje.objects.filter(categoria=cat)
    return render_to_response('comprar_viaje.html',locals(),context_instance=RequestContext(request))

def vista_billetes(request):
    categoria=Categoria.objects.all()
    return render_to_response('billetes.html',locals())
