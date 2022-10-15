from django.urls import path
from django.contrib.auth.views import LogoutView
from WebBlog.views import *

urlpatterns = [
    path('homeWeb/', homeWeb),
    path('', homeWeb),
    path('crear_historia/', crear_historia),
    path('read_historias/', read_historias),
    path('delete_historia/<historia_idDB>', delete_historia),
    path('update_historia/<historia_idDB>', update_historia)


]