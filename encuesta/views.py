from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
	template_name = 'index.html'

class ConsultaView(TemplateView):
	template_name = 'consulta.html'

class AyudaView(TemplateView):
	template_name = 'ayuda.html'



