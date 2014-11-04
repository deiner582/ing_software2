from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from transporte.models import *
from forms import *
# Create your views here.

def vista_index(request):
    iniciar_sesion=Formulario_iniciar_sesion()
    return render_to_response('index.html',locals(),context_instance=RequestContext(request))

def vista_buses(request):
    buses=Autobus.objects.all()
    return render_to_response('buses.html',locals())

def vista_conductores(request):
    cond=Conductor.objects.all()
    return  render_to_response('conductores.html',locals())

def vista_conductor_id(request,id_cond):
    cond=Conductor.objects.get(identificacion=id_cond)
    registro_entrada_salida=Horas_Entrada_Salida.objects.filter(conductor=id_cond)
    historial=Historia_Conductor.objects.filter(conductor=id_cond)
    return render_to_response('condutor_detalle.html',locals(),context_instance=RequestContext(request))

def vista_bus_placa(request,p):
    bus=Autobus.objects.get(placa=p)
    fallosMecanicos = Control_mecanico.objects.filter(autobus_placa=p)
    revisiones = Revisiones_Bus.objects.filter(autobus_placa=p)
    return render_to_response('bus_detalle.html',locals(),context_instance=RequestContext(request))

def comprar_viaje(request,cat):
    billete=Billetes.objects.filter(categoria__codigo__exact='1c')
    return render_to_response('comprar_viaje.html',locals(),context_instance=RequestContext(request))

def vista_registro(request):
    enviado = False
    usuarioRegistrado = False
    nomUsuario =''
    if request.method == 'POST':
        formulario = FormRegistrarUsuario(request.POST)
        if formulario.is_valid():
            try:
                checkUsuario = Usuario.objects.get(identificacion = formulario.cleaned_data['identificacion'])
                nomUsuario = checkUsuario.nombres
                usuarioRegistrado = True
            except ObjectDoesNotExist:
                usuario = Usuario()
                usuario.identificacion = formulario.cleaned_data['identificacion']
                usuario.nombres = formulario.cleaned_data['nombre']
                usuario.apellidos = formulario.cleaned_data['apellido']
                usuario.fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
                usuario.username = formulario.cleaned_data['Username']
                usuario.password = formulario.cleaned_data['Password']
                usuario.puntosAcumulados = 0
                usuario.save()
                enviado = True
    else:
        formulario = FormRegistrarUsuario()
    if enviado :
        formulario = FormRegistrarUsuario()
    ctx = {'form':formulario,'registrado':usuarioRegistrado,'usuario':nomUsuario}
    return render_to_response('registro.html',ctx,context_instance=RequestContext(request))

def vista_billetes(request):
    categoria=Categoria.objects.all()
    return render_to_response('billetes.html',locals())
