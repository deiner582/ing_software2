# -*- encoding: utf-8 -*-
from django import forms
import datetime

class FormRegistrarUsuario(forms.Form):
    identificacion = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control',}))
    Username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}))
    repeterir_Password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}),label="Repetir Password")

class Formulario_iniciar_sesion(forms.Form):
    Username=forms.CharField(widget=forms.TextInput())
    Password = forms.CharField(widget=forms.PasswordInput())
