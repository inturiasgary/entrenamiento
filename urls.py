from django.conf.urls.defaults import *
from bookmarks.views import main_page   #importamos todas las vistas necesarias
from bookmarks.views import user_page
from bookmarks.views import logout_page
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # (r'^django_bookmarks/', include('django_bookmarks.foo.urls')),
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$','django.contrib.auth.views.login'), #para poder interactuar con el logeo de los usuarios, automaticamente ya crea la vista
    (r'^logout/$', logout_page), #pagina donde se cerrara la sesion
    (r'^media/(.*)', 'django.views.static.serve', {'document_root':'site_media'}), #static serve dara acceso a todos los archivos que coloquemos dentro de SITE_MEDIA definido en settings

    # habilitamos la interfaz de administracion
    (r'^admin/(.*)', admin.site.root),
)
