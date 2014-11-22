# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class FormularioRegistro(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'password': forms.PasswordInput(),}

class FormularioLogin(forms.Form):
	usuario = forms.CharField(label='Nombre de Usuario', max_length=100)
	contrasena = forms.CharField(label='Contrasena', widget=forms.PasswordInput)