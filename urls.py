from django.conf.urls.defaults import *
from bookmarks.views import main_page   #importamos todas las vistas necesarias
from bookmarks.views import user_page
from bookmarks.views import logout_page

import os.path #para poder utilizar css

site_media = os.path.join(os.path.dirname(__file__), 'site_media') #dira donde se ubicaran los archivos


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_bookmarks/', include('django_bookmarks.foo.urls')),
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$','django.contrib.auth.views.login'), #para poder interactuar con el logeo de los usuarios, automaticamente ya crea la vista
    (r'^logout/$', logout_page), #pagina donde se cerrara la sesion
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':site_media}), #configuracion para estilos
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
