from django.conf.urls import patterns, url, include
from .views import HomeView, ConsultaView, AyudaView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^consulta$', ConsultaView, name="consulta"),
    url(r'^ayuda$', AyudaView.as_view(), name="ayuda"),
)