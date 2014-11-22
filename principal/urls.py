from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.index', name='index'),
    url(r'^buses/','principal.views.vista_buses',name='buses'),
    url(r'^conductores/','principal.views.vista_conductores',name='conductores'),
    url(r'^billetes/','principal.views.vista_billetes',name='billetes'),
    url(r'^registrar/', 'principal.views.registrar', name='registrar'),
    url(r'^loguear/', 'principal.views.loguear', name='loguear'),
    url(r'^logout_view/', 'principal.views.logout_view', name='logout_view'),
    url(r'^id/(?P<id_cond>.*)$','principal.views.vista_conductor_id',name='conductor detalle'),
    url(r'^placa/(?P<p>.*)$','principal.views.vista_bus_placa',name='bus detalle'),
    url(r'^categoria/(?P<cat>.*)$','principal.views.comprar_viaje',name='comprar viaje'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)