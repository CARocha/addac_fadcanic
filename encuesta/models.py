# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import *
# Create your models here.

class Productores(models.Model):
	nombre = models.CharField('Nombre y apellido', max_length=250)

	class Meta:
		verbose_name= 'Productores'
		verbose_name_plural = 'Productores'

	def __unicode__(self):
		return self.nombre

class Encuesta(models.Model):
	fecha = models.DateField('Fecha de la encuesta', help_text='Introduzca año-mes-dia')
	ano = models.IntegerField('año')
	recolector = models.CharField('Nombre recolector de datos', max_length=250)
	fecha2 = models.DateField('Fecha de ingreso de la encuesta')
	personas = models.CharField('Personas que introdujeron los datos', max_length=250)
	oficina = models.CharField('Oficina de introducción de datos', max_length=50)

	def __unicode__(self):
		return u'%s - %s' % (str(self.fecha),str(self.recolector))

TIPO_CHOICES=((1,'Casa de madera rolliza con techo de paja'),(2,'Casa de madera y techo de paja'),(3,'Casa de madera con techo de zinc'),(4,'Casa minifalda con techo de zinc'),(5,'Casa de concreto con techo de zinc'))
SEXO_PRODUCTOR_CHOICES=((1,'Mujer'),(3,'Hombre'))
AGUA_CHOICES=((1,'Ojo de agua'),(2,'Creeke'),(3,'Pozo con brocal'),(4,'Agua entubada'),(5,'Pozo rustico'),(6,'Agua por gravedad'),(7,'Otros'),(8,'Agua central certificado'),(9,'Pozo rustico sin manejo'))
LEGALIDAD_CHOICES=((1,'Derecho real'),(2,'Derecho procesorio'),(3,'Promesa de venta'),(4,'Titulo de reforma agraria'),(5,'Titulo comunitario'),(6,'Sin documentos'),(7,'Escritura publica'))
DUENO_CHOICES=(('hombre','Hombre'),('mujer','Mujer'),('ambos','Ambos'),('parientes','Parientes'))

class Finca(models.Model):
	nombre_productor = models.ForeignKey(Productores)
	sexo = models.IntegerField('Sexo del productor', choices=SEXO_PRODUCTOR_CHOICES, null = True, blank=True)
	finca = models.CharField("Nombre Finca",max_length=50,null=True,blank=True,help_text='Introduzca nombre de la finca')
	municipio = models.ForeignKey(Municipio,help_text='Introduzca nombre de la municipio')
	microcuenca = models.ForeignKey(Microcuenca,help_text='Introduzca nombre de la microcuenca')
	comunidad = models.ForeignKey(Comunidad,help_text='Introduzca nombre de la comunidad')
	cedula_productor = models.CharField(max_length=25,null=True,blank=True,help_text='Introduzca cedula del productor')
	area_finca = models.DecimalField(max_digits=10,decimal_places=2,help_text='Introduzca el area de la finca en MZ')
	coordenadas_gps = models.DecimalField('Coordenadas Latitud',max_digits=8, decimal_places=6 ,null=True,blank=True,help_text='Introduzca las coordenadas Latitud')
	coordenadas_lg = models.DecimalField('Coordenadas Longitud', max_digits=8, decimal_places=6, null=True, blank=True, help_text="Introduzca las coordenadas Longitud")
	animal_bovino = models.IntegerField(help_text='Introduzca cuantos animales bovinos tiene')
	animal_porcino = models.IntegerField(help_text='Introduzca cuantos animales porcinos tiene')
	animal_equino = models.IntegerField(help_text='Introduzca cuantos animales equinos tiene')
	animal_aves = models.IntegerField(help_text='Introduzca cuantas aves tiene')
	animal_caprino = models.IntegerField(help_text='Introduzca cuantos animales caprino o pelibuey tiene')
	tipo_casa = models.IntegerField(max_length=60,choices=TIPO_CHOICES,help_text='Introduzca que tipo de casa tiene')
	area_casa = models.DecimalField(max_digits=10,decimal_places=2,help_text='Introduzca area de la casa en pie cuadrado')
	fuente_agua = models.IntegerField(max_length=60,choices=AGUA_CHOICES,help_text='Introduzca que fuente de agua tiene')
	legalidad = models.IntegerField(max_length=60,choices=LEGALIDAD_CHOICES, help_text='Introduzca la legalidad de la propiedad')
	propietario = models.CharField(max_length=50,choices=DUENO_CHOICES,help_text='Introduzca el propietario de la finca')

	encuesta = models.ForeignKey(Encuesta)

	def __unicode__(self):
		return self.nombre_productor

	class Meta:
		ordering = ('finca',)
		verbose_name= 'Datos generales de la familia socia'		