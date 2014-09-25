# -*- coding: utf-8 -*-
from django import forms
from .models import Encuesta
from lugar.models import Departamento


def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('ano').values_list('ano', flat=True):
        years.append((en,en))
    return list(set(years))

DUENO_CHOICES = (
          ('', '-------'),
          ('hombre', 'Hombre'),
          ('mujer', 'Mujer'),
          ('ambos', 'Ambos'),
          ('parientes', 'Parientes')
    )

class PrincipalForm(forms.Form):
    fecha = forms.ChoiceField(choices=fecha_choice(),
                              widget=forms.Select(attrs={'class': 'form-control'}))
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
                                          required=False,
                                          widget=forms.Select(attrs={'class': 'form-control'}), 
                                          empty_label="Todos los Departamento")

    municipio = forms.CharField(required=False,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    comunidad = forms.CharField(required=False,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    propietario = forms.ChoiceField(choices=DUENO_CHOICES, 
                                    required=False,
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    repetido = forms.BooleanField(required=False)