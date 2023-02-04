from django.db import models
from django.contrib.auth.models import User


class Noticias(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=1000)
    cuerpo = models.CharField(max_length=1000, null=True)
    fecha_publicacion = models.DateField(null=True)
    autor = models.CharField(max_length=64)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticias')
    imagen_texto = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.titulo}"