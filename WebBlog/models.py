from django.db import models
from django.contrib.auth.models import User

class subirHistoria(models.Model):
    titulo = models.CharField(max_length=40)
    nombreCreador = models.CharField(max_length=40)
    cuerpoHistoria = models.CharField(max_length=9999)
    fechaHistoria = models.DateField()
    
    def __str__(self):
        return f"Titulo:{self.titulo} - Nombre creador:{self.nombreCreador} - Cuerpo historia:{self.cuerpoHistoria} - Fecha historia:{self.fechaHistoria}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares de media
    image = models.ImageField(upload_to="avatares", null = True, blank= True)