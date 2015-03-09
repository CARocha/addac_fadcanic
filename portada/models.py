from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class FotosPortada(models.Model):
    titulo = models.CharField(max_length=250, null=True, blank=True)
    imagen = ImageField(upload_to="portada", blank=True, help_text="Suba su foto aqui")

    class Meta:
        verbose_name = "Foto Portada"
        verbose_name_plural = "Fotos Portadas"

    def __unicode__(self):
        return self.titulo
