from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required #especifica que paginas pueden ser accedidas sin login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from WebBlog.models import *
from WebBlog.forms import *


def homeWeb(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except: 
        avatar = None
    return render(request, "homeWeb.html", {"avatar": avatar})

def homeNoLogin(request):
    return render(request, "homeNoLogin.html")

def crear_historia(request): #its the same what def historias(request): function ---- but for keep order, create again with the others CRUD functions
    if request.method == "POST":
        historia = subirHistoria(titulo = request.POST["titulo"], nombreCreador = request.POST["nombreCreador"], cuerpoHistoria = request.POST["cuerpoHistoria"], fechaHistoria = request.POST["fechaHistoria"])
        historia.save()
        #this read the data in historia DB, and later come back to the link: read_historias.html to show the last added familiar
        historia = subirHistoria.objects.all() #get all data in familiares DB
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except: 
            avatar = None
        return render(request, "historiasCRUD/read_historias.html", {'historia': historia,"avatar": avatar}) #'historias' its the var to use in the template for search
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except: 
        avatar = None
    return render(request, "historiasCRUD/crear_historia.html",{"avatar": avatar}) 


@login_required
def read_historias(request): 
    historias = subirHistoria.objects.all() #get all data in historias DB
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except: 
        avatar = None
    return render(request, "historiasCRUD/read_historias.html", {'historias': historias,"avatar": avatar} )

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

def buscar_historias(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        historia = subirHistoria.objects.filter(titulo__icontains= titulo)
        return render(request, "historiasCRUD/read_historias.html", {'historias_busqueda': historia}) #'historias_busqueda' its the var to use in the template for search
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pw = form.cleaned_data.get("password")

            user = authenticate(username = user, password = pw)

            if user is not None: #si el usuario tiene data (diferente de None)
                login(request, user)
                #return render(request, "home.html")
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except: 
                    avatar = None
                return render(request, "homeWeb.html", {"avatar": avatar})
            else:
                return render(request, "login.html", {"form":form}) #si falla el logeo, te muestra nuevamente los input para iniciar sesion
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def sign_in(request): #register
    form = UserRegisterForm(request.POST) #its inherited from forms.py 
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        
        if form.is_valid():
            #user = form.cleaned_data.get("username")
            form.save()
            return redirect("/WebBlog/login/")
        else:
        #form = UserCreationForm()
            return render(request, "registro.html", {'form': form})
    form = UserRegisterForm()
    return render(request, "registro.html", {"form": form}) #this show the helps with the errors messages

@login_required
def update_profile(request):
    user = request.user
    user_basic_info = User.objects.get(id = user.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = user)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get("usuario")
            user_basic_info.email = form.cleaned_data.get("email")
            user_basic_info.first_name = form.cleaned_data.get("nombre")
            user_basic_info.last_name = form.cleaned_data.get("apellido")
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar = avatar[0].image.url
            except: 
               avatar = None
            return render(request, "homeWeb.html", {"avatar": avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except: 
                avatar = None
            return render(request, "homeWeb.html", {'form': form, "avatar": avatar})
    else:
        form = UserEditForm(initial = {'email': user.email, "usuario": user.username, "nombre": user.first_name, "apellido": user.last_name})
    return render(request, "editarPerfil.html", {'form': form, "user": user})

@login_required
def changePW(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserChangePW(data = request.POST, user = usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except: 
                avatar = None
            return render(request, "homeWeb.html", {"avatar": avatar})
    else:
        form = UserChangePW(request.user)
    return render(request, "changePW.html", {'form': form, "usuario": usuario})    
    
@login_required
def perfil(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except: 
        avatar = None
    return render(request, "perfil.html", {"avatar": avatar})

@login_required
def AgregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data["avatar"], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except: 
                avatar = None
            return render(request, "homeWeb.html", {"avatar": avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except: 
            form = AvatarFormulario()
    return render(request, "AgregarAvatar.html", {"form" : form})