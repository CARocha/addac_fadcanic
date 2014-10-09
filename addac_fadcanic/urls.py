from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^salir/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^', include('encuesta.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )