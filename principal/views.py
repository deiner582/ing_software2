def vista_index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def vista_buses(request):
    buses=Autobus.objects.all()
    return render_to_response('buses.html',locals(),context_instance=RequestContext(request))

def vista_conductores(request):
    cond=Conductor.objects.all()
    return  render_to_response('conductores.html',locals(),context_instance=RequestContext(request))

def vista_conductor_id(request, id_cond):
    cond = Conductor.objects.get(identificacion=id_cond)
    registro_entrada_salida = HoraEntradaSalida.objects.filter(conductor=id_cond)
    historial = HistorialConductor.objects.filter(conductor=id_cond)
    return render_to_response('condutor_detalle.html', locals(), context_instance=RequestContext(request))

def vista_bus_placa(request, p):
    bus = Autobus.objects.get(placa=p)
    fallosMecanicos = ControlMecanico.objects.filter(autobus_placa=p)
    revisiones = RevisionBus.objects.filter(autobus_placa=p)
    return render_to_response('bus_detalle.html', locals(), context_instance=RequestContext(request))


def comprar_viaje(request, cat):
    viaje=Viaje.objects.filter(categoria=cat)
    return render_to_response('comprar_viaje.html',locals(),context_instance=RequestContext(request))

def imprimir_viaje(request, cod):
    viaje=Viaje.objects.get(codigo=cod)
    return render_to_response('imprimir_viaje.html',locals(),context_instance=RequestContext(request))

def pdf(request, cod):
    viaje=Viaje.objects.get(codigo=cod)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=""'+viaje.codigo+".pdf"

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response,portrait(pagesize=A4))


    p.drawImage('estaticos/img/billete.jpg',0,400,width=650,height=300)
    p.drawImage('estaticos/img/transindia.jpg',250,700,width=128,height=128)
    p.setFont('Times-Roman',16)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawCentredString(200,602,viaje.codigo)
    if viaje.tipo=="Ida":
        p.drawCentredString(340,580,"Ida")
        p.drawCentredString(250,570,"$ "+ str(viaje.precio_base_ida))
        p.drawCentredString(280,530,"$ "+ str(viaje.categoria.costo))
        p.drawCentredString(280,505,"$ "+ str(viaje.descuento))
        p.drawCentredString(280,485,"$ "+ str(viaje.precio_total_ida))
    else:
        p.drawCentredString(340,580,"Id y Vu.")
        p.drawCentredString(250,560,"$ "+ str(viaje.precio_base_ida_vuelta))
        p.drawCentredString(280,530,"$ "+ str(viaje.categoria.costo))
        p.drawCentredString(280,505,"$ "+ str(viaje.descuento))
        p.drawCentredString(280,485,"$ "+ str(viaje.precio_total_ida_vuelta))

    p.setFont('Times-Roman',12)
    p.drawCentredString(485,517,str(viaje.origen))
    p.drawCentredString(485,495,str(viaje.destino))
    p.drawCentredString(500,475,str(viaje.categoria.nombre))



    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def vista_registro(request):
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
            return HttpResponseRedirect("/")
    else:
        form = FormularioRegistro()
    return render_to_response('registro.html',locals(), context_instance=RequestContext(request))

def vista_billetes(request):
    categoria=Categoria.objects.all()
    return render_to_response('billetes.html',locals(),context_instance=RequestContext(request))

def vista_iniciar_sesion(request):
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

def vista_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def serializado(request):
    conductor = serializers.serialize("json",Categoria.objects.all())
    return HttpResponse(conductor,content_type="application/json")

def MainHomePage(request):
        return render_to_response('index.html',context_instance=RequestContext(request))



