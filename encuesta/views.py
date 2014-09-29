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

        if 'fecha' in request.session:
            del request.session['fecha']
            del request.session['departamento']
            del request.session['municipio']
            del request.session['comunidad']
            del request.session['propietario']
            request.session['activo'] = False

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
        try:
            perct = cnt * 100 / a.count()
        except:
            perct = 0
        lista1[k] = (cnt,perct)

    frecuencia = a.aggregate(bovino=Count('finca__animal_bovino'),porcino=Count('finca__animal_porcino'),
                       equino=Count('finca__animal_equino'),aves=Count('finca__animal_aves'),
                       caprino=Count('finca__animal_caprino'))
    total = a.aggregate(bovino=Sum('finca__animal_bovino'),porcino=Sum('finca__animal_porcino'),
                       equino=Sum('finca__animal_equino'),aves=Sum('finca__animal_aves'),
                       caprino=Sum('finca__animal_caprino'))
    promedio = a.aggregate(bovino=Avg('finca__animal_bovino'),porcino=Avg('finca__animal_porcino'),
                       equino=Avg('finca__animal_equino'),aves=Avg('finca__animal_aves'),
                       caprino=Avg('finca__animal_caprino'))
    try:
        perct_bovino = frecuencia['bovino']*100/a.count()
    except:
        perct_bovino = 0
    try:
        perct_porcino = frecuencia['porcino']*100/a.count()
    except:
        perct_porcino = 0
    try:
        perct_equino = frecuencia['equino']*100/a.count()
    except:
        perct_equino = 0
    try:
        perct_aves = frecuencia['aves']*100/a.count()
    except:
        perct_aves = 0
    try:
        perct_caprino = frecuencia['caprino']*100/a.count()
    except:
        perct_caprino = 0

    animales = {'Bovino':(frecuencia['bovino'],perct_bovino,total['bovino'],promedio['bovino']),
                'Porcino':(frecuencia['porcino'],perct_porcino,total['porcino'],promedio['porcino']),
                'Equino':(frecuencia['equino'],perct_equino,total['equino'],promedio['equino']),
                'Aves':(frecuencia['aves'],perct_aves,total['aves'],promedio['aves']),
                'Caprino':(frecuencia['caprino'],perct_caprino,total['caprino'],promedio['caprino'])}    

    return render(request, template, {'a':a.count(), 'lista1':lista1, 'animales':animales})

#CBV para la ayuda del sistema
class AyudaView(TemplateView):
    template_name = 'ayuda.html'

#Funcion para graficar (tipo casa) (area de la casa) (fuentes de agua) (legalidad de la propiedad)
# (quien es propietario)tipo_casa,area_casa,fuente_agua,legalidad,propietario
def graficos(request, template="encuesta/detalle_casa.html"):
    a = _query_filtros(request)

    tipo_casa = {}
    for obj in TIPO_CHOICES:
        cnt = a.filter(finca__tipo_casa=obj[0]).count()
        tipo_casa[obj[1]] = cnt
    fuente_agua = {}
    for obj in AGUA_CHOICES:
        cnt = a.filter(finca__fuente_agua=obj[0]).count()
        fuente_agua[obj[1]] = cnt
    legalidad = {}
    for obj in LEGALIDAD_CHOICES:
        cnt = a.filter(finca__legalidad=obj[0]).count()
        legalidad[obj[1]] = cnt
    propietario_casa = {}
    for obj in DUENO_CHOICES:
        cnt = a.filter(finca__propietario=obj[0]).count()
        propietario_casa[obj[1]] = cnt

    rangos = {'0 - mts':(0,0),
              '1 - 5 mts':(0.1,5),
              '5 - 20 mts':(6,20),
              '21 - 50 mts':(21,50),
              '>51 mts':(51,10000),
            }
    area_casa = {} 
    for k,v in rangos.items():
        cnt = a.filter(finca__area_casa__range=v).count()
        area_casa[k] = (cnt)

    return render(request, template, {'tipo_casa':tipo_casa,
                                      'fuente_agua':fuente_agua,
                                      'legalidad':legalidad,
                                      'propietario_casa':propietario_casa,
                                      'area_casa':area_casa,
                                      'a':a.count()})

#Funcion para mostrar los datos de la educacion
def educacion(request, template="encuesta/educacion.html"):
    a = _query_filtros(request)

    tabla_educacion = []
    grafo = []
    suma = 0
    for e in SEXO_CHOICE:
        objeto = a.filter(educacion__sexo_edad = e[0]).aggregate(num_total = Sum('educacion__num_persona'),
                                                            nosabe_leer = Sum('educacion__nosabe_leer'),
                                                            p_incompleta = Sum('educacion__pri_incompleta'),
                                                            p_completa = Sum('educacion__pri_completa'),
                                                            s_incompleta = Sum('educacion__secu_incompleta'),
                                                            s_completa = Sum('educacion__secu_completa'),
                                                            uni_o_tecnico = Sum('educacion__uni_o_tecnico'),
                                                            estudiando = Sum('educacion__estudiando'))
        try:
            suma = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['s_completa'] or 0) + int(objeto['uni_o_tecnico'] or 0) + int(objeto['estudiando'] or 0)
        except:
            pass
        variable = round(saca_porcentajes(suma,objeto['num_total']))
        grafo.append([e[1],variable])
        fila = [e[1], objeto['num_total'],
                saca_porcentajes(objeto['nosabe_leer'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                 saca_porcentajes(objeto['s_completa'], objeto['num_total'], False),
                saca_porcentajes(objeto['uni_o_tecnico'], objeto['num_total'], False),
                saca_porcentajes(objeto['estudiando'], objeto['num_total'], False),
                ]
        tabla_educacion.append(fila)
    tabla_eba = {}
    for obj in SEXO_CHOICE:
        cnt_finalizado = a.filter(educacion__sexo_edad = obj[0],educacion__circ_estudio_adulto=1).count()
        cnt_activo = a.filter(educacion__sexo_edad = obj[0],educacion__circ_estudio_adulto=2).count()
        tabla_eba[obj[1]] = (cnt_finalizado, cnt_activo)

    print tabla_eba
    return render(request, template, {'tabla_educacion':tabla_educacion,'grafo':grafo,
                                      'a':a.count(), 'tabla_eba':tabla_eba})
#urls de los indicadores
VALID_VIEWS = {
        'generales': generales,
        'detalle_casas': graficos,
        'educacion': educacion,
        
}
# Función para obtener las url
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))

def saca_porcentajes(dato, total, formato=True):
    '''Si formato es true devuelve float caso contrario es cadena'''
    if dato != None:
        try:
            porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
        except:
            return 0
        if formato:
            return porcentaje
        else:
            return '%.2f' % porcentaje
    else:
        return 0