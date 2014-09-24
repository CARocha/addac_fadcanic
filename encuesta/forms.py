# -*- coding: utf-8 -*-
from django import forms
from .models import Encuesta, Finca
from lugar.models import Departamento, Municipio, Comunidad, Microcuenca


def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('ano').values_list('ano', flat=True):
        years.append((en,en))
    return list(set(years))

class PrincipalForm(forms.Form):
    fecha = forms.ChoiceField(choices=fecha_choice())
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
                                          required=False, 
                                          label=u'Departamentos')
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all().order_by('nombre'), 
                                       required=False)
    comunidad = forms.ModelChoiceField(queryset=Comunidad.objects.all(), 
                                       required=False)
    repetido = forms.BooleanField(required=False)