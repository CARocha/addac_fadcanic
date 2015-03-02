# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Select
from .models import *
from lugar.models import Departamento, Municipio, Comunidad
from lookups import *
from selectable.forms import AutoCompleteSelectField
import selectable.forms as selectable

class ProductorAdminForm(forms.ModelForm):

    class Meta(object):
        model = Finca
        widgets = {
            'nombre_productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
        }

class FormSeguridadPProcesados(ModelForm):
    
    class Meta:
        model = SeguridadPProcesados
        widgets = {
            'producto': Select(attrs={'class': 'chosen-select'}),
        }

class FormSeguridadSaf(ModelForm):
    
    class Meta:
        model = SeguridadSaf
        #widgets = {
        #    'cultivos': Select(attrs={'class': 'select2'}),
        #}

class FormSeguridadCAnuales(ModelForm):
    
    class Meta:
        model = SeguridadCAnuales
        widgets = {
            'cultivos': Select(attrs={'class': 'chosen-select'}),
        }

class FormSeguridadPAnimal(ModelForm):
    
    class Meta:
        model = SeguridadPAnimal
        widgets = {
            'producto': Select(attrs={'class': 'chosen-select'}),
        }

class FormIngresoServicioNegocio(ModelForm):
    
    class Meta:
        model = IngresoServicioNegocio
        widgets = {
            'servicios': Select(attrs={'class': 'chosen-select'}),
        }

class FormCredito(ModelForm):
    
    class Meta:
        model = Credito
        widgets = {
            'organizacion': Select(attrs={'class': 'chosen-select'}),
        }

class FormSeguridadAlimentaria(ModelForm):
    
    class Meta:
        model = SeguridadAlimentaria
        widgets = {
            'alimentos': Select(attrs={'class': 'chosen-select'}),
        }

class FormInnovacion(ModelForm):
    
    class Meta:
        model = Innovacion
        widgets = {
            'innovacion': Select(attrs={'class': 'chosen-select'}),
        }

def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('-ano').values_list('ano', flat=True):
        years.append((en,en))
    return sorted(list(set(years)))

DUENO_CHOICES = (
          ('', '-------'),
          ('hombre', 'Hombre'),
          ('mujer', 'Mujer'),
          ('ambos', 'Ambos'),
          ('parientes', 'Parientes')
    )
REPETIDO_CHOICES = (
          ('', '-------'),
          ('1', '1 Año'),
          ('2', '2 Años'),
          ('3', '3 Años'),
          ('4', '4 Años')
    )

class PrincipalForm(forms.Form):
    fecha = forms.MultipleChoiceField(choices=fecha_choice())
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
                                          required=False,
                                          widget=forms.Select(attrs={'class': 'form-control'}), 
                                          empty_label="Todos los Departamento")

    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), required=False,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    comunidad = forms.ModelChoiceField(queryset=Comunidad.objects.all(), required=False,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    propietario = forms.ChoiceField(choices=DUENO_CHOICES, 
                                    required=False,
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    repetido = forms.ChoiceField(choices=REPETIDO_CHOICES, 
                                    required=False,
                                    widget=forms.Select(attrs={'class': 'form-control'}))