from django.conf.urls import patterns, url
from .views import HomeView, AyudaView

urlpatterns = patterns('encuesta.views',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^consulta/$', 'ConsultaView', name="consulta"),
    url(r'^ayuda/$', AyudaView.as_view(), name="ayuda"),
    url(r'^(?P<vista>\w+)/$', '_get_view'),
)