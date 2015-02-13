from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=40)
    
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __unicode__(self):
        return u'%s - %s' % (self.departamento, self.nombre)

class Comunidad(models.Model):
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Comunidad'
        verbose_name_plural = 'Comunidades'

    def __unicode__(self):
        return self.nombre

class Microcuenca(models.Model):
    comunidad = models.ForeignKey(Comunidad,null=True,blank=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Microcuenca'
        verbose_name_plural = 'Microcuencas'

    def __unicode__(self):
        return self.nombre
