from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from transporte.models import *
from forms import *
# Create your views here.

def vista_index(request):
    iniciar_sesion=Formulario_iniciar_sesion()
    return render_to_response('index.html',locals())

def vista_buses(request):
    buses=Autobus.objects.all()
    return render_to_response('buses.html',locals())

def vista_conductores(request):
    cond=Conductor.objects.all()
    return  render_to_response('conductores.html',locals())

def vista_registro(request):
    if request.method == 'POST':
        formulario = FormRegistrarUsuario(request.POST)
        if formulario.is_valid():
            usuario = Usuario()
            usuario.identificacion = formulario.cleaned_data['identificacion']
            usuario.nombres = formulario.cleaned_data['nombre']
            usuario.apellidos = formulario.cleaned_data['apellido']
            usuario.fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
            usuario.username=formulario.cleaned_data['Username']
            usuario.password=formulario.cleaned_data['Password']
            usuario.puntosAcumulados = 0
            usuario.save()
    else:
        formulario = FormRegistrarUsuario()
    ctx = {'form':formulario}
    return render_to_response('registro.html',ctx,context_instance=RequestContext(request))

def vista_billetes(request):
    categoria=Categoria.objects.all()
    return render_to_response('billetes.html',locals())