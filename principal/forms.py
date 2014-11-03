# -*- encoding: utf-8 -*-
from django import forms
import datetime

class FormRegistrarUsuario(forms.Form):
    identificacion = forms.IntegerField(widget=forms.TextInput())
    nombre = forms.CharField(widget=forms.TextInput())
    apellido = forms.CharField(widget=forms.TextInput())
    fecha_nacimiento = forms.DateField(widget=forms.DateInput())