# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ViewDoesNotExist
from .models import *
from .forms import *
from django.db.models import Count, Sum, Avg

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
    rangos = {'0 - mz':(0,0),
              '0.1 - 5 mz':(0.1,5),
              '5 - 20 mz':(6,20),
              '21 - 50 mz':(21,50),
              '>51 mz':(51,10000),
            }
    lista1 = {} 
    for k,v in rangos.items():
        cnt = a.filter(finca__area_finca__range=v).count()
        perct = cnt * 100 / a.count()
        lista1[k] = (cnt,perct)

    frecuencia = a.aggregate(bovino=Count('finca__animal_bovino'),porcino=Count('finca__animal_porcino'),
                       equino=Count('finca__animal_equino'),aves=Count('finca__animal_aves'),
                       caprino=Count('finca__animal_caprino'))

    print frecuencia
    total = a.aggregate(bovino=Sum('finca__animal_bovino'),porcino=Sum('finca__animal_porcino'),
                       equino=Sum('finca__animal_equino'),aves=Sum('finca__animal_aves'),
                       caprino=Sum('finca__animal_caprino'))
    print total
    promedio = a.aggregate(bovino=Avg('finca__animal_bovino'),porcino=Avg('finca__animal_porcino'),
                       equino=Avg('finca__animal_equino'),aves=Avg('finca__animal_aves'),
                       caprino=Avg('finca__animal_caprino'))
    print promedio

    animales = {'Bovino':(frecuencia['bovino'],frecuencia['bovino']*100/a.count(),total['bovino'],promedio['bovino']),
                'Porcino':(frecuencia['porcino'],frecuencia['porcino']*100/a.count(),total['porcino'],promedio['porcino']),
                'Equino':(frecuencia['equino'],frecuencia['equino']*100/a.count(),total['equino'],promedio['equino']),
                'Aves':(frecuencia['aves'],frecuencia['aves']*100/a.count(),total['aves'],promedio['aves']),
                'Caprino':(frecuencia['caprino'],frecuencia['caprino']*100/a.count(),total['caprino'],promedio['caprino'])}    
    print animales

    return render(request, template, {'a':a.count(), 'lista1':lista1, 'animales':animales})

#CBV para la ayuda del sistema
class AyudaView(TemplateView):
    template_name = 'ayuda.html'

#urls de los indicadores

VALID_VIEWS = {
        'generales': generales,
        
}
# Función para obtener las url
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))
