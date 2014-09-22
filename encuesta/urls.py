from django.conf.urls import patterns, url, include
from .views import HomeView, ConsultaView, AyudaView

urlpatterns = patterns('',
    (r'^$', HomeView.as_view()),
    (r'^consulta$', ConsultaView.as_view()),
    (r'^ayuda$', AyudaView.as_view()),
)