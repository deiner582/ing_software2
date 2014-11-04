# -*- encoding: utf-8 -*-
from django import forms
import datetime

class FormRegistrarUsuario(forms.Form):
    identificacion = forms.IntegerField(widget=forms.TextInput())
    nombre = forms.CharField(widget=forms.TextInput())
    apellido = forms.CharField(widget=forms.TextInput())
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))
    Username=forms.CharField(widget=forms.TextInput())
    Password = forms.CharField(widget=forms.PasswordInput())
    repeterir_Password=forms.CharField(widget=forms.PasswordInput(),label="Repetir Password")

class Formulario_iniciar_sesion(forms.Form):
    Username=forms.CharField(widget=forms.TextInput())
    Password = forms.CharField(widget=forms.PasswordInput())

