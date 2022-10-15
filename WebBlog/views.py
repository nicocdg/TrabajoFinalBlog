
from django.http import HttpResponse
from django.template import loader
from WebBlog.models import *
from WebBlog.forms import *
from django.shortcuts import render, redirect
# Create your views here.


def homeWeb(request):
    return render(request, "homeWeb.html")

def crear_historia(request): #its the same what def historias(request): function ---- but for keep order, create again with the others CRUD functions
    if request.method == "POST":
        historia = subirHistoria(titulo = request.POST["titulo"], nombreCreador = request.POST["nombreCreador"], cuerpoHistoria = request.POST["cuerpoHistoria"], fechaHistoria = request.POST["fechaHistoria"])
        historia.save()

        #this read the data in Familiares DB, and later come back to the link: read_familiares.html to show the last added familiar
        historia = subirHistoria.objects.all() #get all data in familiares DB
        return render(request, "historiasCRUD/read_historias.html", {'historia': historia}) #'familiares' its the var to use in the template for search

    return render(request, "historiasCRUD/crear_historia.html") 

#@login_required #necesita estar logeado para acceder a esta funcion, si no, nos enviará a la pagina de login debido a la configuracion que hicimos en settings.py
def read_historias(request): 
    historias = subirHistoria.objects.all() #get all data in historias DB
    return render(request, "historiasCRUD/read_historias.html", {'historias': historias}) #'historias' its the var to use in the template for search

def delete_historia(request, historia_idDB): 
    historia = subirHistoria.objects.get(id = historia_idDB) #can use (nombre = historia_nombre), but if I have multiple historias in the db with the same name I will get a error, so instead of that I use "id" what is a hidden object parameter in the db
    historia.delete()

    #this read the data in historias DB, and later come back to the link: read_historias.html to show the last added familiar
    historias = subirHistoria.objects.all() #get all data in historias DB
    return render(request, "historiasCRUD/read_historias.html", {'historias': historias}) #'historias' its the var to use in the template for search

def update_historia(request, historia_idDB): 
    historia = subirHistoria.objects.get(id = historia_idDB)

    if request.method == "POST":
        formulario =form_historias(request.POST) #get form_familiares from forms.py

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            historia.titulo = informacion["titulo"]    
            historia.nombreCreador = informacion["nombreCreador"] 
            historia.cuerpoHistoria = informacion["cuerpoHistoria"] 
            historia.fechaHistoria = informacion["fechaHistoria"] 
            historia.save()
            historias = subirHistoria.objects.all()
            return render(request, "historiasCRUD/read_historias.html", {'historias': historias})
    else:
        formulario = form_historias(initial={"titulo": historia.titulo,"nombreCreador": historia.nombreCreador,"cuerpoHistoria": historia.cuerpoHistoria,"fechaHistoria": historia.fechaHistoria})
    return render(request, "historiasCRUD/update_historia.html", {"formulario": formulario})