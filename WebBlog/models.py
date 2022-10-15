from django.db import models

class subirHistoria(models.Model):
    titulo = models.CharField(max_length=40)
    nombreCreador = models.CharField(max_length=40)
    cuerpoHistoria = models.CharField(max_length=9999)
    fechaHistoria = models.DateField()

    #hecho en clase 22, si entro en administracion y a la tabla de familiares, ahora me muestra directamente los datos guardados, en vez de tener que entrar al object y ver que data tiene dentro.
    def __str__(self):
        return f"Titulo:{self.titulo} - Nombre creador:{self.nombreCreador} - Cuerpo historia:{self.cuerpoHistoria} - Fecha historia:{self.fechaHistoria}"
