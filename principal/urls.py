from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'principal.views.vista_index', name='Home'),
    url(r'^buses/','principal.views.vista_buses',name='buses'),
    url(r'^conductores/','principal.views.vista_conductores',name='conductores'),
    url(r'^registro/','principal.views.vista_registro',name='conductores'),
    url(r'^billetes/','principal.views.vista_billetes',name='billetes'),
    url(r'^conductores/id/(?P<id_cond>.*)$','principal.views.vista_conductor_id',name='conductor detalle'),
    url(r'^admin/', include(admin.site.urls)),
)
