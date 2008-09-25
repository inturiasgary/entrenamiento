# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect ,Http404 #necesario para trabajar con templates
from django.contrib.auth import logout #para poder cerrar el logeo de los usuarios
from django.contrib.auth.models import User #necesario para trabajar con usuarios
from django.shortcuts import render_to_response #para poder hacer la validaciones de usuario
from django.template import Context #error autocomplementacion de texto "minuscula"
from django.template.loader import get_template #para poder convertir un archivo html a template

from django.template import RequestContext #para facilitar el trabajo de acceso de logins

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({               #variables que enviaremos al template, context convierte a diccionario
        'head_title':'Django Bookmarks',
        'page_title':'Welcome to django bookmarks',
        'page_body':'Where you can store all perrita'
        })
    #output = template.render(variables) #para realizar la conversion del template a html
    return render_to_response('main_page.html', RequestContext(request))

    #return render_to_response('main_page.html', { 'user':request.user }) #retornamos el html #

def user_page(request, username):
    try:
        user=User.objects.get(username=username) #obtenemos el usuario del cual queremos mostrar la informacion
    except:
        raise Http404('no te encuentras!!!') #si no existe mostramos la pagina 404
    bookmarks = user.bookmark_set.all() #obtenemos todos los bookmarks del respectivo usuario
    template = get_template('user_page.html')
    variables = RequestContext(request,{
        'username':username,
        'bookmarks':bookmarks
    })
    output = template.render(variables)
    return render_to_response('user_page.html' ,variables)
    #return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')