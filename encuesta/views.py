from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import *

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


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
    
    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    
    if request.session['repetido'] == True:
        return Encuesta.objects.filter(**params).filter(finca__repetido=True)
    else:
        return Encuesta.objects.filter(**params)


def ConsultaView(request, template='consulta.html'):

    if request.method == 'POST':
        mensaje = None
        form = PrincipalForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['comunidad'] = form.cleaned_data['comunidad']
            mensaje = "Variables correctamentas :)"
            request.session['activo'] = True
            centinela = 1
            return HttpResponseRedirect("/")
        else:
            centinela = 0            
    else:
        form = PrincipalForm()
        mensaje = "Existen errores"
        centinela = 0
        if 'fecha' in request.session:
            del request.session['fecha']
            del request.session['departamento']
            del request.session['municipio']
            del request.session['comunidad']

    render(request, template, locals())

class AyudaView(TemplateView):
    template_name = 'ayuda.html'



