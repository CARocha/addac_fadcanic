# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.core.exceptions import ViewDoesNotExist
from .models import *
from .forms import PrincipalForm, fecha_choice, FormMapa
from django.db.models import Sum, Avg
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import json as simplejson
from portada.models import FotosPortada

# CBV para el home y los graficos


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
# nuevas salidas
# fotos de la portada
        context['fotos'] = FotosPortada.objects.all()
# por ADDAC
        context['addac_hombres'] = Productores.objects.filter(
            sexo=3, pertenece=2).count()
        context['addac_mujeres'] = Productores.objects.filter(
            sexo=1, pertenece=2).count()
        context['addac_activos'] = Productores.objects.filter(
            pertenece=2, activo=1).count()
        context['addac_inactivos'] = Productores.objects.filter(
            pertenece=2, activo=2).count()
        context['addac_jovenes'] = Productores.objects.filter(
            pertenece=2, edad__range=(16, 25)).count()
        context['addac_adultos'] = Productores.objects.filter(
            pertenece=2, edad__gte=26).count()
        context['addac_promedio_mz'] = Encuesta.objects.filter(
            finca__nombre_productor__pertenece=2).aggregate(
            Avg('finca__area_finca'))
        lista_encuestas_addac = {}
        for year in fecha_choice():
            num_anio = Encuesta.objects.filter(ano=year[0],
                                               finca__nombre_productor__pertenece=2).count()
            lista_encuestas_addac[year[1]] = num_anio
        context['addac_num_encuestas'] = lista_encuestas_addac
# por FADCANIC
        context['fad_hombres'] = Productores.objects.filter(
            sexo=3, pertenece=1).count()
        context['fad_mujeres'] = Productores.objects.filter(
            sexo=1, pertenece=1).count()
        context['fad_activos'] = Productores.objects.filter(
            pertenece=1, activo=1).count()
        context['fad_inactivos'] = Productores.objects.filter(
            pertenece=1, activo=2).count()
        context['fad_jovenes'] = Productores.objects.filter(
            pertenece=1, edad__range=(16, 25)).count()
        context['fad_adultos'] = Productores.objects.filter(
            pertenece=1, edad__gte=26).count()
        context['fad_promedio_mz'] = Encuesta.objects.filter(
            finca__nombre_productor__pertenece=1).aggregate(
            Avg('finca__area_finca'))
        lista_encuestas_fad = {}
        for year in fecha_choice():
            num_anio = Encuesta.objects.filter(ano=year[0],
                                               finca__nombre_productor__pertenece=2).count()
            lista_encuestas_fad[year[1]] = num_anio
        context['addac_num_encuestas'] = lista_encuestas_fad


# empienzan los graficos de los anios
# analfabetismo
        # SEXO_CHOICE_3 = (
        #     (1,'Hombres de 25 adelante'),
        #     (2,'Mujeres de 25 adelante'),
        #     (3,'Hombres Jóvenes de 15 a 24'),
        #     (4,'Mujeres Jóvenes de 15 a 24'),
        #     (5,'Hombres adolescentes de 9 a 14'),
        #     (6,'Mujeres adolescentes de 9 a 14'),)
        # anios = fecha_choice()
        # analfabetismo_addac = {}
        # for e in SEXO_CHOICE_3:
        #     obj_2009 = Encuesta.objects.filter(educacion__sexo_edad = e[0],finca__comunidad__municipio__departamento=5, ano=2009).aggregate(Sum('educacion__nosabe_leer'))['educacion__nosabe_leer__sum']
        #     obj_2011 = Encuesta.objects.filter(educacion__sexo_edad = e[0],finca__comunidad__municipio__departamento=5, ano=2011).aggregate(Sum('educacion__nosabe_leer'))['educacion__nosabe_leer__sum']
        #     obj_2013 = Encuesta.objects.filter(educacion__sexo_edad = e[0],finca__comunidad__municipio__departamento=5, ano=2013).aggregate(Sum('educacion__nosabe_leer'))['educacion__nosabe_leer__sum']
        #     analfabetismo_addac[e[1]] = (obj_2009,obj_2011,obj_2013)
        # context['analfabetismo_addac'] = analfabetismo_addac

        # analfabetismo_fad = {}
        # for e in SEXO_CHOICE_3:
        #     obj_2009 = Encuesta.objects.filter(educacion__sexo_edad = e[0],finca__comunidad__municipio__departamento=3, ano=2009).aggregate(Sum('educacion__nosabe_leer'))['educacion__nosabe_leer__sum']
        #     obj_2011 = Encuesta.objects.filter(educacion__sexo_edad = e[0],finca__comunidad__municipio__departamento=3, ano=2011).aggregate(Sum('educacion__nosabe_leer'))['educacion__nosabe_leer__sum']
        #     obj_2013 = Encuesta.objects.filter(educacion__sexo_edad = e[0],finca__comunidad__municipio__departamento=3, ano=2013).aggregate(Sum('educacion__nosabe_leer'))['educacion__nosabe_leer__sum']
        #     if obj_2011 != 0:
        #         obj_2011 = 0
        #     analfabetismo_fad[e[1]] = (obj_2009,obj_2011,obj_2013)
        # context['analfabetismo_fad'] = analfabetismo_fad

        # #propiedades sin documentos
        # legalidad_addac = {}
        # for year in fecha_choice():
        #     legal  = Finca.objects.filter(legalidad = 6,comunidad__municipio__departamento=5, encuesta__ano=year[0]).count()
        #     legalidad_addac[year[1]] = legal
        # context['legalidad_addac'] = legalidad_addac

        # legalidad_fadcanic = {}
        # for year in fecha_choice():
        #     legal  = Finca.objects.filter(legalidad = 6,comunidad__municipio__departamento=3, encuesta__ano=year[0]).count()
        #     legalidad_fadcanic[year[1]] = legal
        # context['legalidad_fadcanic'] = legalidad_fadcanic

        # #Dueños de la propiedad
        # DUENO_CHOICES_3 = (
        #     ('hombre','Hombre'),
        #     ('mujer','Mujer'),
        #     ('ambos','Ambos'),
        #     ('parientes','Parientes')
        #     )
        # propietario_addac = {}
        # for obj in DUENO_CHOICES_3:
        #     obj_2009 = Finca.objects.filter(propietario = obj[0],comunidad__municipio__departamento=5, encuesta__ano=2009).count()
        #     obj_2011 = Finca.objects.filter(propietario = obj[0],comunidad__municipio__departamento=5, encuesta__ano=2011).count()
        #     obj_2013 = Finca.objects.filter(propietario = obj[0],comunidad__municipio__departamento=5, encuesta__ano=2013).count()
        #     propietario_addac[obj[1]] = (obj_2009,obj_2011,obj_2013)
        # context['propietario_addac'] = propietario_addac

        # propietario_fadcanic = {}
        # for obj in DUENO_CHOICES_3:
        #     obj_2009 = Finca.objects.filter(propietario = obj[0],encuesta__finca__comunidad__municipio__departamento=3, encuesta__ano=2009).count()
        #     obj_2011 = Finca.objects.filter(propietario = obj[0],encuesta__finca__comunidad__municipio__departamento=3, encuesta__ano=2011).count()
        #     obj_2013 = Finca.objects.filter(propietario = obj[0],encuesta__finca__comunidad__municipio__departamento=3, encuesta__ano=2013).count()
        #     propietario_fadcanic[obj[1]] = (obj_2009,obj_2011,obj_2013)
        # context['propietario_fadcanic'] = propietario_fadcanic

        # #Uso de credito
        # credito_addac = {}
        # for obj in UsoCredito.objects.all():
        #     obj_2009 = Encuesta.objects.filter(credito__uso=obj,finca__comunidad__municipio__departamento=5, ano=2009).count()
        #     obj_2011 = Encuesta.objects.filter(credito__uso=obj,finca__comunidad__municipio__departamento=5, ano=2011).count()
        #     obj_2013 = Encuesta.objects.filter(credito__uso=obj,finca__comunidad__municipio__departamento=5, ano=2013).count()
        #     credito_addac[obj] = (obj_2009,obj_2011,obj_2013)
        # context['credito_addac'] = credito_addac

        # credito_fadcanic = {}
        # for obj in UsoCredito.objects.all():
        #     obj_2009 = Encuesta.objects.filter(credito__uso=obj,finca__comunidad__municipio__departamento=3, ano=2009).count()
        #     obj_2011 = Encuesta.objects.filter(credito__uso=obj,finca__comunidad__municipio__departamento=3, ano=2011).count()
        #     obj_2013 = Encuesta.objects.filter(credito__uso=obj,finca__comunidad__municipio__departamento=3, ano=2013).count()
        #     credito_fadcanic[obj] = (obj_2009,obj_2011,obj_2013)
        # context['credito_fadcanic'] = credito_fadcanic

        return context


def mostrar_productores(request, organizacion_id=None,
                        sexo_id=None, template='encuesta/lista_productores.html'):

    personas = {}
    for obj in Comunidad.objects.all():
        query = Finca.objects.filter(comunidad=obj,
                                     nombre_productor__pertenece=organizacion_id,
                                     nombre_productor__sexo=sexo_id,
                                     nombre_productor__activo=1).distinct()
        if query:
            personas[obj] = query

    return render(request, template, locals())


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
        params['ano__in'] = request.session['fecha']
    if request.session['comunidad']:
        params['finca__comunidad'] = request.session['comunidad']
    if request.session['municipio']:
        params['finca__comunidad__municipio'] = request.session['municipio']
    if request.session['departamento']:
        params['finca__comunidad__municipio__departamento'] = request.session[
            'departamento']

    if request.session['propietario']:
        params['finca__propietario'] = request.session['propietario']

    # if request.session['repetido'] == True:
    #    return Encuesta.objects.filter(**params).filter(finca__repetido=True)
    # else:
    return Encuesta.objects.filter(**params)

# funcion para el formulario de la consulta


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
            centinela = 0
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

    return render(request, template, {'form': form, 'centinela': centinela})

# funcion para el primer indicador


def generales(request, template='encuesta/generales.html'):
    query = _query_filtros(request)
    a = query.count()

    cero = query.filter(finca__area_finca__range=(0, 0)).count()
    cinco = query.filter(finca__area_finca__range=(0.1, 5.99)).count()
    veinte = query.filter(finca__area_finca__range=(6, 20.99)).count()
    cincuenta = query.filter(finca__area_finca__range=(21, 50.99)).count()
    mas = query.filter(finca__area_finca__range=(51, 1000000)).count()
    otros = a - (cero + cinco + veinte + cincuenta + mas)
    cero2 = cero + otros

    rangos = {'0 - mz': (0, 0),
              '0.1 - 5 mz': (0.1, 5.99),
              '6 - 20 mz': (6, 20.99),
              '21 - 50 mz': (21, 50.99),
              '>51 mz': (51, 1000000),
              }
    lista1 = {}
    for k, v in rangos.items():
        cnt = query.filter(finca__area_finca__range=v).count()
        try:
            perct = cnt * 100 / a.count()
        except:
            perct = 0
        lista1[k] = (cnt, perct)

    total_fincas = query.count()
    # TODO: Frecuencia de animales
    bovino = query.filter(finca__animal_bovino__gt=0).count()
    porcino = query.filter(finca__animal_porcino__gt=0).count()
    equino = query.filter(finca__animal_equino__gt=0).count()
    aves = query.filter(finca__animal_aves__gt=0).count()
    caprino = query.filter(finca__animal_caprino__gt=0).count()
    # TODO: Porcentajes de los animales
    por_bovino = (float(bovino) / total_fincas) * \
        100 if total_fincas != 0 else 0
    por_porcino = (float(porcino) / total_fincas) * \
        100 if total_fincas != 0 else 0
    por_equino = (float(equino) / total_fincas) * \
        100 if total_fincas != 0 else 0
    por_aves = (float(aves) / total_fincas) * 100 if total_fincas != 0 else 0
    por_caprino = (float(caprino) / total_fincas) * \
        100 if total_fincas != 0 else 0
    # TODO: totales por animales
    sum_bovino = query.aggregate(Sum('finca__animal_bovino'))
    sum_porcino = query.aggregate(Sum('finca__animal_porcino'))
    sum_equino = query.aggregate(Sum('finca__animal_equino'))
    sum_aves = query.aggregate(Sum('finca__animal_aves'))
    sum_caprino = query.aggregate(Sum('finca__animal_caprino'))
    # TODO: promedio de los animales
    pro_bovino = query.filter(
        finca__animal_bovino__gt=0).aggregate(
        Avg('finca__animal_bovino'))
    pro_porcino = query.filter(
        finca__animal_porcino__gt=0).aggregate(
        Avg('finca__animal_porcino'))
    pro_equino = query.filter(
        finca__animal_equino__gt=0).aggregate(
        Avg('finca__animal_equino'))
    pro_aves = query.filter(
        finca__animal_aves__gt=0).aggregate(
        Avg('finca__animal_aves'))
    pro_caprino = query.filter(
        finca__animal_caprino__gt=0).aggregate(
        Avg('finca__animal_caprino'))

    return render(request, template, locals())

# CBV para la ayuda del sistema


class AyudaView(TemplateView):
    template_name = 'ayuda.html'

# Funcion para graficar (tipo casa) (area de la casa) (fuentes de agua) (legalidad de la propiedad)
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

    rangos = {'0 - mts': (0, 0),
              '1 - 5 mts': (0.1, 5.99),
              '5 - 20 mts': (6, 20.99),
              '21 - 50 mts': (21, 50.99),
              '>51 mts': (51, 10000000),
              }
    area_casa = {}
    for k, v in rangos.items():
        cnt = a.filter(finca__area_casa__range=v).count()
        area_casa[k] = (cnt)

    return render(request, template, {'tipo_casa': tipo_casa,
                                      'fuente_agua': fuente_agua,
                                      'legalidad': legalidad,
                                      'propietario_casa': propietario_casa,
                                      'area_casa': area_casa,
                                      'a': a.count()})

# Funcion para mostrar los datos de la educacion


def educacion(request, template="encuesta/educacion.html"):
    a = _query_filtros(request)

    tabla_educacion = []
    grafo = []
    suma = 0
    for e in SEXO_CHOICE:
        objeto = a.filter(educacion__sexo_edad=e[0]).aggregate(num_total=Sum('educacion__num_persona'),
                                                               nosabe_leer=Sum(
                                                                   'educacion__nosabe_leer'),
                                                               p_incompleta=Sum(
                                                                   'educacion__pri_incompleta'),
                                                               p_completa=Sum(
                                                                   'educacion__pri_completa'),
                                                               s_incompleta=Sum(
                                                                   'educacion__secu_incompleta'),
                                                               s_completa=Sum(
                                                                   'educacion__secu_completa'),
                                                               uni_o_tecnico=Sum(
                                                                   'educacion__uni_o_tecnico'),
                                                               estudiando=Sum('educacion__estudiando'))
        try:
            suma = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto[
                's_completa'] or 0) + int(objeto['uni_o_tecnico'] or 0) + int(objeto['estudiando'] or 0)
        except:
            pass
        variable = round(saca_porcentajes(suma, objeto['num_total']))
        grafo.append([e[1], variable])
        fila = [e[1], objeto['num_total'],
                saca_porcentajes(
            objeto['nosabe_leer'],
            objeto['num_total'],
            False),
            saca_porcentajes(
            objeto['p_incompleta'],
            objeto['num_total'],
            False),
            saca_porcentajes(
            objeto['p_completa'],
            objeto['num_total'],
            False),
            saca_porcentajes(
            objeto['s_incompleta'],
            objeto['num_total'],
            False),
            saca_porcentajes(objeto['s_completa'], objeto['num_total'], False),
            saca_porcentajes(
            objeto['uni_o_tecnico'],
            objeto['num_total'],
            False),
            saca_porcentajes(
            objeto['estudiando'],
            objeto['num_total'],
            False),
        ]
        tabla_educacion.append(fila)

    tabla_eba = {}
    for obj in SEXO_CHOICE:
        cnt_finalizado = a.filter(educacion__sexo_edad=obj[0]).aggregate(estudia_eba=Sum('educacion__estu_eba'),
                                                                         estu_mined=Sum(
                                                                             'educacion__estu_mined'),
                                                                         estu_uni=Sum(
                                                                             'educacion__estu_uni'),
                                                                         egresado_eba=Sum(
                                                                             'educacion__egresado_eba'),
                                                                         egresado_mined=Sum(
                                                                             'educacion__egresado_mined'),
                                                                         )
        tabla_eba[obj[1]] = (cnt_finalizado)

    pintar = tabla_eba["Hombres de 25 adelante"]["estudia_eba"]

    return render(request, template, {'tabla_educacion': tabla_educacion, 'grafo': grafo,
                                      'a': a.count(), 'tabla_eba': tabla_eba, 'pintar': pintar})

# Función para mostrar los datos de credito su uso y con quien tiene.


def credito(request, template="encuesta/credito.html"):
    a = _query_filtros(request)

    tiene_credito = []
    for obj in OrganizacionesDanCredito.objects.all():
        cnt = a.filter(credito__organizacion=obj).count()
        tiene_credito.append((obj.nombre, cnt))

    uso_credito = []
    for obj in UsoCredito.objects.all():
        cnt = a.filter(credito__uso=obj).count()
        beneficiarios = a.filter(
            credito__uso=obj).aggregate(
            beneficiarios=Sum('credito__personas'))
        uso_credito.append((obj.nombre, cnt, beneficiarios))

    return render(request, template, {'a': a.count(), 'tiene_credito': tiene_credito,
                                      'uso_credito': uso_credito})


# Función para mostrar datos de uso de tierra (anterior sistema era
# cobertura boscosa)

def uso_tierra(request, template="encuesta/uso_tierra.html"):
    a = _query_filtros(request)

    suma = a.aggregate(total_uso=Sum('usotierra__total_uso'),
                       bosque_primario=Sum('usotierra__bosque_primario'),
                       bosque_secundario=Sum('usotierra__bosque_secundario'),
                       tacotales=Sum('usotierra__tacotal'),
                       cultivos_perennes=Sum('usotierra__cultivos_perennes'),
                       cultivos_semiperennes=Sum(
                           'usotierra__cultivos_semiperennes'),
                       cultivos_anuales=Sum('usotierra__cultivos_anuales'),
                       potrero_sin_arboles=Sum(
                           'usotierra__potrero_sin_arboles'),
                       potrero_arboles=Sum('usotierra__potrero_arboles'),
                       plantaciones_forestales=Sum(
                           'usotierra__plantaciones_forestales'),
                       )

    dicc_one = {
        'total_uso': {'usotierra__total_uso__gt': 0},
        'bosque_primario': {'usotierra__bosque_primario__gt': 0},
        'bosque_secundario': {'usotierra__bosque_secundario__gt': 0},
        'tacotales': {'usotierra__tacotal__gt': 0},
        'cultivos_perennes': {'usotierra__cultivos_perennes__gt': 0},
        'cultivos_semiperennes': {'usotierra__cultivos_semiperennes__gt': 0},
        'cultivos_anuales': {'usotierra__cultivos_anuales__gt': 0},
        'potrero_sin_arboles': {'usotierra__potrero_sin_arboles__gt': 0},
        'potrero_arboles': {'usotierra__potrero_arboles__gt': 0},
        'plantaciones_forestales': {'usotierra__plantaciones_forestales__gt': 0}
    }
    results = {}
    for k, v in dicc_one.items():
        results[k] = a.filter(**v).count()

    resultados = []
    lista_llaves = sorted(suma.keys())
    for key in lista_llaves:
        fila = []  # [key, conteo, porcentaje, sumatoria manzanas, porcentaje area, cobertura]
        fila.append(key.replace('_', ' ').capitalize())
        # conteo de las areas
        fila.append(results[key])
        porcentaje_conteo = (
            float(
                results[key]) / results['total_uso']) * 100 if results['total_uso'] != 0 else 0
        fila.append("%.2f" % porcentaje_conteo)
        fila.append(suma[key])
        porcentaje_area = (
            float(
                suma[key]) / suma['total_uso']) * 100 if suma['total_uso'] != 0 else 0
        fila.append("%.2f" % porcentaje_area)
        resultados.append(fila)

    resultados2 = []
    for obj in resultados:
        if obj[0] != "Total uso":
            resultados2.append(obj)
    try:
        porcentaje_cobertura_boscosa = (((float(suma['bosque_primario']) * 1) + (float(suma['cultivos_anuales']) * 0.5) +
                                         (float(suma['bosque_secundario']) * 0.7) + (float(suma['cultivos_perennes']) * 0.5) +
                                         (float(suma['cultivos_semiperennes']) * 0.5) + (float(suma['tacotales']) * 0.5) +
                                         (float(suma['potrero_sin_arboles']) * 0.5) + (float(suma['plantaciones_forestales']) * 1) +
                                         (float(suma['potrero_arboles']) * 0.3)) / float(suma['total_uso'])) * 100
        porcentaje_cobertura_boscosa = "%.2f" % porcentaje_cobertura_boscosa
    except:
        porcentaje_cobertura_boscosa = 0

    return render(request, template, {'a': a.count(), 'data': resultados,
                                      'porcentaje_cobertura': porcentaje_cobertura_boscosa, 'resultados2': resultados2})

# conteo de cuanta gente compra los alimentos por clasificacion


def compran_productos(request, id_clasificacion):
    a = _query_filtros(request)

    conteo = 0
    for obj in AlimentosSeguridad.objects.filter(
            clasificacion=id_clasificacion):
        conteo = a.filter(seguridadalimentaria__alimentos=obj,
                          seguridadalimentaria__comprar=True).count()

    return conteo

# Funcion para calcular la seguridad alimentaria


def seguridad_alimentaria(
        request, template="encuesta/seguridad_alimentaria.html"):
    a = _query_filtros(request)

    productos_sa = {}
    clasificacion = {}
    for obj in AlimentosSeguridad.objects.all():
        compran = a.filter(
            seguridadalimentaria__alimentos=obj,
            seguridadalimentaria__comprar=True).count()
        diario = a.filter(
            seguridadalimentaria__alimentos=obj,
            seguridadalimentaria__consumo=1).count()
        semanal = a.filter(
            seguridadalimentaria__alimentos=obj,
            seguridadalimentaria__consumo=2).count()
        ocasional = a.filter(
            seguridadalimentaria__alimentos=obj,
            seguridadalimentaria__consumo=3).count()
        no = a.filter(
            seguridadalimentaria__alimentos=obj,
            seguridadalimentaria__consumo=4).count()

        productos_sa[obj] = (compran, diario, semanal, ocasional, no)

    carbohidrato = compran_productos(request, 1)
    vitaminas = compran_productos(request, 2)
    grasas = compran_productos(request, 3)
    proteinas = compran_productos(request, 4)
    minerales = compran_productos(request, 5)

    return render(request, template, {'a': a.count(), 'productos_sa': productos_sa,
                                      'carbohidrato': carbohidrato,
                                      'vitaminas': vitaminas, 'grasas': grasas,
                                      'proteinas': proteinas, 'minerales': minerales})

# Función sobre las innovaciones en la finca


def innovaciones(request, template="encuesta/innovaciones.html"):
    a = _query_filtros(request)
    conteo = {}
    for obj in TipoInnovacion.objects.all().order_by('nombre'):
        si = a.filter(innovacion__innovacion=obj, innovacion__aplica=1).count()
        no = a.filter(innovacion__innovacion=obj, innovacion__aplica=2).count()
        conteo[obj.nombre] = (si, no)

    return render(request, template, {'a': a.count(), 'data': conteo})

# Funcion sobre ingreso en cultivos anuales


def ingreso_anuales(request, template="encuesta/ingresos_anuales.html"):
    a = _query_filtros(request)

    anuales = {}
    for obj in CultivosAnuales.objects.all():
        cnt = a.filter(seguridadcanuales__cultivos=obj).aggregate(
            total_manzanas=Sum('seguridadcanuales__area_produccion'),
            total_prudccion=Sum('seguridadcanuales__produccion'),
            total_autoconsumo=Sum('seguridadcanuales__auto_consumo'),
            total_perdida=Sum('seguridadcanuales__perdidas'),
            venta_no=Sum('seguridadcanuales__venta_no'),
            precio_no=Avg('seguridadcanuales__precio_promedio_no'),
            venta_organizada=Sum('seguridadcanuales__venta_organizada'),
            precio_organizado=Avg('seguridadcanuales__precio_promedio_orga'))
        if cnt['total_manzanas'] > 0:
            anuales[obj] = cnt

    return render(request, template, {'a': a.count(), 'data': anuales})

# Funcion sobre ingreso en pruductos animales


def ingreso_animal(request, template="encuesta/ingresos_animales.html"):
    a = _query_filtros(request)

    animales = {}
    for obj in CHOICE_ANIAMLES:
        cnt = a.filter(seguridadpanimal__producto=obj[0]).aggregate(total_produccion=Sum('seguridadpanimal__produccion'),
                                                                    total_autoconsumo=Sum(
                                                                        'seguridadpanimal__auto_consumo'),
                                                                    total_perdida=Sum(
                                                                        'seguridadpanimal__perdidas'),
                                                                    venta_no=Sum(
                                                                        'seguridadpanimal__venta_no'),
                                                                    precio_no=Avg(
                                                                        'seguridadpanimal__precio_promedio_no'),
                                                                    venta_organizada=Sum(
                                                                        'seguridadpanimal__venta_organizada'),
                                                                    precio_organizado=Avg('seguridadpanimal__precio_promedio_orga'))
        if cnt['total_produccion'] > 0:
            animales[obj[1]] = cnt
    # grafico para quien manejo el negocio
    grafo_maneja = {}
    for obj in CHOICE_MANEJA:
        cnt = a.filter(seguridadpanimal__maneja=obj[0]).count()
        grafo_maneja[obj[1]] = cnt
    # grafico para ver si tienen plan de negocio
    # grafo_plan = {}
    # for obj in CHOICE_PLAN_NEGOCIO:
    #     cnt = a.filter(seguridadpanimal__plan_negocio=obj[0]).count()
    #     grafo_plan[obj[1]] = cnt

    return render(request, template, {'a': a.count(), 'data': animales})

# Funcion sobre ingreso en pruductos animales


def ingreso_pprocesados(request, template="encuesta/ingresos_pprocesado.html"):
    a = _query_filtros(request)

    animales = {}
    for obj in CHOICE_PRODUCTOS_PROCESADOS:
        cnt = a.filter(seguridadpprocesados__producto=obj[0]).aggregate(total_produccion=Sum('seguridadpprocesados__produccion'),
                                                                        total_autoconsumo=Sum(
                                                                            'seguridadpprocesados__auto_consumo'),
                                                                        total_perdida=Sum(
                                                                            'seguridadpprocesados__perdidas'),
                                                                        venta_no=Sum(
                                                                            'seguridadpprocesados__venta_no'),
                                                                        precio_no=Avg(
                                                                            'seguridadpprocesados__precio_promedio_no'),
                                                                        venta_organizada=Sum(
                                                                            'seguridadpprocesados__venta_organizada'),
                                                                        )
        if cnt['total_produccion'] > 0:
            animales[obj[1]] = cnt
    # grafico para quien manejo el negocio
    grafo_maneja = {}
    for obj in CHOICE_MANEJA:
        cnt = a.filter(seguridadpprocesados__maneja=obj[0]).count()
        grafo_maneja[obj[1]] = cnt
    # grafico para ver si tienen plan de negocio
    # grafo_plan = {}
    # for obj in CHOICE_PLAN_NEGOCIO:
    #     cnt = a.filter(seguridadpprocesados__plan_negocio=obj[0]).count()
    #     grafo_plan[obj[1]] = cnt

    return render(request, template, {'a': a.count(), 'data': animales})

# Funcion sobre ingreso en pruductos animales


def ingreso_negocio(request, template="encuesta/ingresos_negocio.html"):
    a = _query_filtros(request)

    animales = {}
    for obj in ServiciosActividades.objects.all():
        cnt = a.filter(ingresoservicionegocio__servicios=obj).aggregate(cantidad=Sum('ingresoservicionegocio__cantidad'),
                                                                        precio=Avg(
                                                                            'ingresoservicionegocio__precio'),
                                                                        ingresos=Sum(
                                                                            'ingresoservicionegocio__ingresos'),
                                                                        )
        if cnt['cantidad'] > 0:
            animales[obj.__str__] = cnt
    # grafico para quien manejo el negocio
    grafo_maneja = {}
    for obj in CHOICE_MANEJA:
        cnt = a.filter(ingresoservicionegocio__maneja=obj[0]).count()
        grafo_maneja[obj[1]] = cnt
    # grafico para ver si tienen plan de negocio
    grafo_plan = {}
    for obj in CHOICE_PLAN_NEGOCIO:
        cnt = a.filter(ingresoservicionegocio__plan_negocio=obj[0]).count()
        grafo_plan[obj[1]] = cnt

    return render(request, template, {'a': a.count(), 'data': animales})

# Funcion sobre ingreso en pruductos saf


def ingreso_saf(request, template="encuesta/ingresos_negocio.html"):
    a = _query_filtros(request)

    saf = {}
    for obj in SISTEMAS_CHOICES:
        cnt = a.filter(seguridadsaf__cultivos=obj[0]).aggregate(area_desarrollo=Sum('seguridadsaf__area_desarrollo'),
                                                                area_produccion=Sum(
                                                                    'seguridadsaf__area_produccion'),
                                                                produccion_total=Sum(
                                                                    'seguridadsaf__produccion_total'),
                                                                auto_consumo=Sum(
                                                                    'seguridadsaf__auto_consumo'),
                                                                perdidas=Sum(
                                                                    'seguridadsaf__perdidas'),
                                                                venta_no=Sum(
                                                                    'seguridadsaf__venta_no'),
                                                                precio_promedio_no=Avg(
                                                                    'seguridadsaf__precio_promedio_no'),
                                                                venta_organizada=Sum(
                                                                    'seguridadsaf__venta_organizada'),
                                                                precio_promedio_orga=Avg(
                                                                    'seguridadsaf__precio_promedio_orga'),
                                                                )
        if cnt['area_desarrollo'] > 0:
            saf[obj[1]] = cnt

    return render(request, template, {'a': a.count(), 'data': saf})


def busquedaProductor(request):
    if request.is_ajax():
        productor = Productores.objects.filter(nombre__icontains = request.GET['nombre'] ).values('nombre', 'id')
        return HttpResponse( simplejson.dumps( list(productor)), mimetype='application/json' )
    else:
        return HttpResponse("Solo Ajax");


def mapa(request, template="encuesta/mapa.html"):
    #a = _query_filtros(request)
    form = FormMapa()

    return render(request, template, {'form':form})

# urls de los indicadores
VALID_VIEWS = {
    'entrar': entrar,
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
    'ingreso_saf': ingreso_saf,
    'mapa': mapa,

}
# Función para obtener las url


def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist(
            "Tried %s in module %s Error: View not defined in VALID_VIEWS." %
            (vista, 'encuesta.views'))


def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento=departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
    return HttpResponse(simplejson.dumps(
        lista), mimetype='application/javascript')


def get_comunidad(request, municipio):
    comunidades = Comunidad.objects.filter(municipio=municipio)
    lista = [(comunidad.id, comunidad.nombre) for comunidad in comunidades]
    return HttpResponse(simplejson.dumps(
        lista), mimetype='application/javascript')


def saca_porcentajes(dato, total, formato=True):
    '''Si formato es true devuelve float caso contrario es cadena'''
    if dato is not None:
        try:
            porcentaje = (dato / float(total)) * \
                100 if total is not None or total != 0 else 0
        except:
            return 0
        if formato:
            return porcentaje
        else:
            return '%.2f' % porcentaje
    else:
        return 0
