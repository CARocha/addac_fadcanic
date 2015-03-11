from django.conf.urls import patterns, url
from .views import HomeView, AyudaView

urlpatterns = patterns('encuesta.views',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^consulta/$', 'ConsultaView', name="consulta"),
    url(r'^ayuda/$', AyudaView.as_view(), name="ayuda"),
    url(r'^(?P<vista>\w+)/$', '_get_view'),
    url(r'^consulta/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    url(r'^consulta/ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    url(r'^lista/(?P<organizacion_id>\d+)/(?P<sexo_id>\d+)/$', 'mostrar_productores'),
)