from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'addac_fadcanic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('encuesta.urls')), 
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )