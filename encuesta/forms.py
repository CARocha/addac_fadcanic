# -*- coding: utf-8 -*-
from django import forms
from .models import Encuesta, Productores, Finca
from lugar.models import Departamento
from lookups import *
from selectable.forms import AutoCompleteSelectField
import selectable.forms as selectable

class ProductorAdminForm(forms.ModelForm):
    nombre_productor = selectable.AutoCompleteSelectField(lookup_class=ProductorLookup, allow_new=True)

    class Meta(object):
        model = Finca
        widgets = {
            'nombre_productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
        }
        #exclude = ('nombre_productor', )

    # def __init__(self, *args, **kwargs):
    #     super(ProductorAdminForm, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.pk and self.instance.nombre_productor:
    #         self.initial['nombre_productor'] = self.instance.nombre_productor.pk

    # def save(self, *args, **kwargs):
    #     nombre_productor = self.cleaned_data['nombre_productor']
    #     if nombre_productor and not nombre_productor.pk:
    #         nombre_productor = Productores.objects.create(nombre=nombre_productor.nombre,)
    #     self.instance.nombre_productor = nombre_productor
    #     return super(ProductorAdminForm, self).save(*args, **kwargs)



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