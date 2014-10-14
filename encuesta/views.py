# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.exceptions import ViewDoesNotExist
from .models import *
from .forms import *
from django.db.models import Count, Sum, Avg
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# CBV para el home y los graficos
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form1'] = AuthenticationForm()

        return context

def entrar(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        login(request, form.get_user())
        return HttpResponseRedirect('/')
    else:
        return redirect('/admin')

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

#Función para mostrar los datos de credito su uso y con quien tiene.
def credito(request, template="encuesta/credito.html"):
    a = _query_filtros(request)

    tiene_credito = []
    for obj in OrganizacionesDanCredito.objects.all():
        cnt = a.filter(credito__organizacion = obj).count()
        tiene_credito.append((obj.nombre, cnt))

    uso_credito = []
    for obj in UsoCredito.objects.all():
        cnt = a.filter(credito__uso = obj).count()
        beneficiarios = a.filter(credito__uso = obj).aggregate(beneficiarios=Sum('credito__personas'))
        uso_credito.append((obj.nombre, cnt, beneficiarios))

    return render(request, template, {'a':a.count(), 'tiene_credito':tiene_credito,
                                      'uso_credito':uso_credito})


#Función para mostrar datos de uso de tierra (anterior sistema era cobertura boscosa)

def uso_tierra(request, template="encuesta/uso_tierra.html"):
    a = _query_filtros(request)

    suma = a.aggregate(total_uso = Sum('usotierra__total_uso'),
                        bosque_primario = Sum('usotierra__bosque_primario'),
                        bosque_secundario= Sum('usotierra__bosque_secundario'),
                        tacotales = Sum('usotierra__tacotal'), 
                        cultivos_perennes = Sum('usotierra__cultivos_perennes'), 
                        cultivos_semiperennes = Sum('usotierra__cultivos_semiperennes'), 
                        cultivos_anuales = Sum('usotierra__cultivos_anuales'), 
                        potrero_sin_arboles = Sum('usotierra__potrero_sin_arboles'), 
                        potrero_arboles = Sum('usotierra__potrero_arboles'),
                        plantaciones_forestales= Sum('usotierra__plantaciones_forestales'),
                    )
    #print suma
    dicc_one = {
        'total_uso': {'usotierra__total_uso__gt': 0 },
        'bosque_primario': {'usotierra__bosque_primario__gt': 0 },
        'bosque_secundario':{'usotierra__bosque_secundario__gt': 0 },
        'tacotales':{'usotierra__tacotal__gt': 0 },
        'cultivos_perennes':{'usotierra__cultivos_perennes__gt': 0 },
        'cultivos_semiperennes':{'usotierra__cultivos_semiperennes__gt': 0 },
        'cultivos_anuales':{'usotierra__cultivos_anuales__gt': 0 },
        'potrero_sin_arboles': {'usotierra__potrero_sin_arboles__gt': 0 }, 
        'potrero_arboles': {'usotierra__potrero_arboles__gt': 0 },
        'plantaciones_forestales': {'usotierra__plantaciones_forestales__gt': 0 }
    }
    results = {}
    for k, v in dicc_one.items():
        results[k] = a.filter(**v).count()
    #print results
    resultados = []
    lista_llaves = suma.keys()
    lista_llaves.sort()
    for key in lista_llaves:
        fila = [] # [key, conteo, porcentaje, sumatoria manzanas, porcentaje area, cobertura]
        fila.append(key.replace('_', ' ').capitalize())
        #conteo de las areas
        fila.append(results[key])
        porcentaje_conteo = (float(results[key])/results['total_uso'])*100 if results['total_uso']!=0 else 0
        fila.append("%.2f" % porcentaje_conteo)
        fila.append(suma[key])
        porcentaje_area = (float(suma[key])/suma['total_uso'])*100 if suma['total_uso']!= 0  else 0
        fila.append("%.2f" % porcentaje_area)
        resultados.append(fila)
    
    return render(request, template, {'a':a.count(),'data':resultados})

#Funcion para calcular la seguridad alimentaria
def seguridad_alimentaria(request, template="encuesta/seguridad_alimentaria.html"):
    a = _query_filtros(request)
    id_alimentos = [dato[0] for dato in ALIMENTO_CHOICES] 
    total_encuestas=a.count() #usado para el porcentaje
    datos = []
    resultados = []
    for id in id_alimentos:
        datos = a.filter(seguridadalimentaria__alimentos=id).aggregate(compran=Sum('seguridadalimentaria__comprar'))
        for key in datos.keys():
            if datos[key]==None:
                datos[key]=0
        nivel_consumo = a.filter(seguridadalimentaria__alimentos=id,
                                 seguridadalimentaria__nivel_consumo_suficiente=2).aggregate(nivel=Count('seguridadalimentaria'))
        fila=[] #[alimento, compran, porcentaje,nivel consumo,porcentaje]
        fila.append(ALIMENTO_CHOICES[id-1][1])
        fila.append(datos['compran'])
        porcentaje = (float(datos['compran'])/total_encuestas)*100
        fila.append("%.2f" % porcentaje) 
        fila.append(nivel_consumo['nivel'])
        porcentaje = (float(nivel_consumo['nivel'])/total_encuestas)*100
        fila.append("%.2f" % porcentaje) 
        resultados.append(fila)
    return render(request, template, {'a':a.count(), 'data':resultados})

#Función sobre las innovaciones en la finca
def innovaciones(request, template="encuesta/innovaciones.html"):
    a = _query_filtros(request)
    conteo = {}
    total_si = 0
    total_no = 0
    for obj in TipoInnovacion.objects.all().order_by('nombre'):
        si = a.filter(innovacion__innovacion=obj, innovacion__aplica=1).count()
        total_si += si
        no = a.filter(innovacion__innovacion=obj, innovacion__aplica=2).count()
        total_no += no
        conteo[obj.nombre] = (si/a.count()*100, no/a.count()*100)

    return render(request, template, {'a':a.count(), 'data': conteo})

#Funcion sobre ingreso en cultivos anuales
def ingreso_anuales(request, template="encuesta/ingresos_anuales.html"):
    a = _query_filtros(request)

    anuales = {}
    for obj in SISTEMAS_CHOICES:
        cnt = a.filter(seguridadcanuales__cultivos=obj[0]).aggregate(total_manzanas=Sum('seguridadcanuales__area_produccion'),
                                                                    total_prudccion=Sum('seguridadcanuales__produccion'),
                                                                    total_autoconsumo=Sum('seguridadcanuales__auto_consumo'),
                                                                    total_perdida=Sum('seguridadcanuales__perdidas'),
                                                                    venta_no=Sum('seguridadcanuales__venta_no'),
                                                                    precio_no=Avg('seguridadcanuales__precio_promedio_no'),
                                                                    venta_organizada=Sum('seguridadcanuales__venta_organizada'),
                                                                    precio_organizado=Avg('seguridadcanuales__precio_promedio_orga'))
        if cnt['total_manzanas'] > 0:
            anuales[obj[1]] = cnt
    
    return render(request, template, {'a':a.count(), 'data':anuales})

#Funcion sobre ingreso en pruductos animales
def ingreso_animal(request, template="encuesta/ingresos_animales.html"):
    a = _query_filtros(request)

    animales = {}
    for obj in CHOICE_ANIAMLES:
        cnt = a.filter(seguridadpanimal__producto=obj[0]).aggregate(total_produccion=Sum('seguridadpanimal__produccion'),
                                                                    total_autoconsumo=Sum('seguridadpanimal__auto_consumo'),
                                                                    total_perdida=Sum('seguridadpanimal__perdidas'),
                                                                    venta_no=Sum('seguridadpanimal__venta_no'),
                                                                    precio_no=Avg('seguridadpanimal__precio_promedio_no'),
                                                                    venta_organizada=Sum('seguridadpanimal__venta_organizada'),
                                                                    precio_organizado=Avg('seguridadpanimal__precio_promedio_orga'))
        if cnt['total_produccion'] > 0:
            animales[obj[1]] = cnt
    #grafico para quien manejo el negocio
    grafo_maneja = {}
    for obj in CHOICE_MANEJA:
        cnt = a.filter(seguridadpanimal__maneja=obj[0]).count()
        grafo_maneja[obj[1]] = cnt
    #grafico para ver si tienen plan de negocio
    grafo_plan = {}
    for obj in CHOICE_PLAN_NEGOCIO:
        cnt = a.filter(seguridadpanimal__plan_negocio=obj[0]).count()
        grafo_plan[obj[1]] = cnt

    return render(request, template, {'a':a.count(), 'data':animales})

#Funcion sobre ingreso en pruductos animales
def ingreso_pprocesados(request, template="encuesta/ingresos_pprocesado.html"):
    a = _query_filtros(request)

    animales = {}
    for obj in CHOICE_PRODUCTOS_PROCESADOS:
        cnt = a.filter(seguridadpprocesados__producto=obj[0]).aggregate(total_produccion=Sum('seguridadpprocesados__produccion'),
                                                                    total_autoconsumo=Sum('seguridadpprocesados__auto_consumo'),
                                                                    total_perdida=Sum('seguridadpprocesados__perdidas'),
                                                                    venta_no=Sum('seguridadpprocesados__venta_no'),
                                                                    precio_no=Avg('seguridadpprocesados__precio_promedio_no'),
                                                                    venta_organizada=Sum('seguridadpprocesados__venta_organizada'),
                                                                    )
        if cnt['total_produccion'] > 0:
            animales[obj[1]] = cnt
    #grafico para quien manejo el negocio
    grafo_maneja = {}
    for obj in CHOICE_MANEJA:
        cnt = a.filter(seguridadpprocesados__maneja=obj[0]).count()
        grafo_maneja[obj[1]] = cnt
    #grafico para ver si tienen plan de negocio
    grafo_plan = {}
    for obj in CHOICE_PLAN_NEGOCIO:
        cnt = a.filter(seguridadpprocesados__plan_negocio=obj[0]).count()
        grafo_plan[obj[1]] = cnt

    return render(request, template, {'a':a.count(), 'data':animales})

#Funcion sobre ingreso en pruductos animales
def ingreso_negocio(request, template="encuesta/ingresos_negocio.html"):
    a = _query_filtros(request)

    animales = {}
    for obj in ServiciosActividades.objects.all():
        cnt = a.filter(ingresoservicionegocio__servicios=obj).aggregate(cantidad=Sum('ingresoservicionegocio__cantidad'),
                                                                    precio=Avg('ingresoservicionegocio__precio'),
                                                                    ingresos=Sum('ingresoservicionegocio__ingresos'),
                                                                    )
        if cnt['cantidad'] > 0:
            animales[obj.__str__] = cnt
    #grafico para quien manejo el negocio
    grafo_maneja = {}
    for obj in CHOICE_MANEJA:
        cnt = a.filter(ingresoservicionegocio__maneja=obj[0]).count()
        grafo_maneja[obj[1]] = cnt
    #grafico para ver si tienen plan de negocio
    grafo_plan = {}
    for obj in CHOICE_PLAN_NEGOCIO:
        cnt = a.filter(ingresoservicionegocio__plan_negocio=obj[0]).count()
        grafo_plan[obj[1]] = cnt

    return render(request, template, {'a':a.count(), 'data':animales})

#urls de los indicadores
VALID_VIEWS = {
        'entrar':entrar,
        'generales': generales,
        'detalle_casas': graficos,
        'educacion': educacion,
        'credito': credito,
        'tierra': uso_tierra,
        'seguridad_alimentaria': seguridad_alimentaria,
        'innovacion': innovaciones,
        'cultivos_anuales': ingreso_anuales,
        'ingreso_animal': ingreso_animal,
        'ingreso_procesados': ingreso_pprocesados,
        'ingreso_negocio': ingreso_negocio,
        
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