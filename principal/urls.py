from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'principal.views.vista_index', name='Home'),
    url(r'^buses/','principal.views.vista_buses',name='buses'),
    url(r'^conductores/','principal.views.vista_conductores',name='conductores'),
    url(r'^conductor/json/','principal.views.serializado',name='json'),
    url(r'^login/','principal.views.vista_iniciar_sesion',name='iniciar sesion'),
    url(r'^logout/','principal.views.vista_logout',name='logout'),
    url(r'^registro/','principal.views.vista_registro',name='conductores'),
    url(r'^billetes/','principal.views.vista_billetes',name='billetes'),
    url(r'^id/(?P<id_cond>.*)$','principal.views.vista_conductor_id',name='conductor detalle'),
    url(r'^placa/(?P<p>.*)$','principal.views.vista_bus_placa',name='bus detalle'),
    url(r'^categoria/(?P<cat>.*)$','principal.views.comprar_viaje',name='comprar viaje'),
    url(r'^viaje/(?P<cod>.*)$','principal.views.imprimir_viaje',name='imprimir viaje'),
    url(r'^pdf/(?P<cod>.*)$','principal.views.pdf',name='pdf'),
    url(r'^admin/', include(admin.site.urls)),
)
