from django.shortcuts import render
from django.shortcuts import render_to_response
from transporte.models import *
# Create your views here.

def vista_index(request):
    auto=autobus.objects.all()
    return render_to_response('index.html',{'a':auto})
