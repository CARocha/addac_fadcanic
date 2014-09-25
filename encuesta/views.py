# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import *


# Función para obtener las url
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))

# CBV para el home y los graficos
class HomeView(TemplateView):
    template_name = 'index.html'

# funcion para los filtros automaticos
def _query_filtros(request):
    params = {}
    if 'fecha' in request.session:
        params['ano'] = request.session['fecha']
    if request.session['comunidad']:
        params['finca__comunidad'] = request.session['comunidad']
    if request.session['municipio']:
        params['finca__comunidad__municipio'] = request.session['municipio']
    if request.session['departamento']:
        params['finca__comunidad__municipio__departamento'] = request.session['departamento']
               
    if request.session['propietario']:
        params['finca__propietario'] = request.session['propietario']
    
    
    print params
    #if request.session['repetido'] == True:
    #    return Encuesta.objects.filter(**params).filter(finca__repetido=True)
    #else:
    return Encuesta.objects.filter(**params)

#funcion para el formulario de la consulta
def ConsultaView(request, template='consulta.html'):
    if request.method == 'POST':
        form = PrincipalForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['comunidad'] = form.cleaned_data['comunidad']
            request.session['propietario'] = form.cleaned_data['propietario']
            request.session['repetido'] = form.cleaned_data['repetido'] 
            request.session['activo'] = True
            centinela = 1
    else:
        form = PrincipalForm()
        centinela = 0

        #if 'fecha' in request.session:
        #    del request.session['fecha']
        #    del request.session['departamento']
        #    del request.session['municipio']
        #    del request.session['comunidad']

    return render(request, template, {'form':form,'centinela':centinela})

#funcion para el primer indicador
def generales(request, template='encuesta/generales.html'):
    a = _query_filtros(request)
    return render(request, template, {'a':a.count()})

#CBV para la ayuda del sistema
class AyudaView(TemplateView):
    template_name = 'ayuda.html'

VALID_VIEWS = {
        'generales': generales,
        
    }


