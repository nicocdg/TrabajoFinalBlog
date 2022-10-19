from django.urls import path
from django.contrib.auth.views import LogoutView
from WebBlog.views import *
from WebBlog.forms import *

urlpatterns = [
    path('homeWeb/', homeWeb),
    path('homeNoLogin', homeNoLogin),
    path('', homeNoLogin),
    path('crear_historia/', crear_historia),
    path('read_historias/', read_historias),
    path('buscar_historias/', buscar_historias),
    path('delete_historia/<historia_idDB>', delete_historia),
    path('update_historia/<historia_idDB>', update_historia),
    path('login/', login_request),
    path('sign_in/', sign_in),
    path('logout/', LogoutView.as_view(template_name = "homeNoLogin.html"), name = "Sesion cerrada"),
    path('editarPerfil/', update_profile),
    path('changePW/', changePW),
    path('perfil/', perfil),
    path('changeAvatar/', AgregarAvatar)
]