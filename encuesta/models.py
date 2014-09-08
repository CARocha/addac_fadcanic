# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import *
from smart_selects.db_fields import ChainedForeignKey 

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

TIPO_CHOICES = (
    (1,'Casa de madera rolliza con techo de paja'),
    (2,'Casa de madera y techo de paja'),
    (3,'Casa de madera con techo de zinc'),
    (4,'Casa minifalda con techo de zinc'),
    (5,'Casa de concreto con techo de zinc')
)
SEXO_PRODUCTOR_CHOICES = (
    (1,'Mujer'),
    (3,'Hombre')
)
AGUA_CHOICES = (
    (1,'Ojo de agua'),
    (2,'Creeke'),
    (3,'Pozo con brocal'),
    (4,'Agua entubada'),
    (5,'Pozo rustico'),
    (6,'Agua por gravedad'),
    (7,'Otros'),
    (8,'Agua central certificado'),
    (9,'Pozo rustico sin manejo')
    )
LEGALIDAD_CHOICES = (
    (1,'Derecho real'),
    (2,'Derecho procesorio'),
    (3,'Promesa de venta'),
    (4,'Titulo de reforma agraria'),
    (5,'Titulo comunitario'),
    (6,'Sin documentos'),
    (7,'Escritura publica')
    )
DUENO_CHOICES = (
    ('hombre','Hombre'),
    ('mujer','Mujer'),
    ('ambos','Ambos'),
    ('parientes','Parientes')
    )
#---------------------------------------------------------------------------
#      Modelo: Datos generales de las familias socias
#---------------------------------------------------------------------------

class Finca(models.Model):
    nombre_productor = models.ForeignKey(Productores)
    sexo = models.IntegerField('Sexo del productor', choices=SEXO_PRODUCTOR_CHOICES, null = True, blank=True)
    finca = models.CharField("Nombre Finca",max_length=50,null=True,blank=True,help_text='Introduzca nombre de la finca')
    municipio = models.ForeignKey(Municipio, help_text='Introduzca nombre de la municipio', 
                                 related_name="municipio")
    comunidad = ChainedForeignKey(
        Comunidad, 
        chained_field="municipio",
        chained_model_field="municipio", 
        show_all=False, 
        auto_choose=True
    )
    microcuenca = ChainedForeignKey(
        Microcuenca, 
        chained_field="comunidad",
        chained_model_field="comunidad", 
        show_all=False, 
        auto_choose=True
    )
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

#-------------------------------------------------------------
#     uso de la tierra
#-------------------------------------------------------------

class UsoTierra(models.Model):
    bosque_primario = models.DecimalField(max_digits=10,decimal_places=2)
    primario_observacion = models.CharField('Observaciones', max_length=250)
    bosque_secundario = models.DecimalField(max_digits=10,decimal_places=2)
    secundario_observacion = models.CharField('Observaciones', max_length=250)
    tacotal =  models.DecimalField(max_digits=10,decimal_places=2)
    tacotal_observacion = models.CharField('Observaciones', max_length=250)
    cultivos_perennes = models.DecimalField(max_digits=10,decimal_places=2)
    perennes_observacion = models.CharField('Observaciones', max_length=250)
    cultivos_semiperennes = models.DecimalField(max_digits=10,decimal_places=2)
    semiperennes_observacion = models.CharField('Observaciones', max_length=250)
    cultivos_anuales = models.DecimalField(max_digits=10,decimal_places=2)
    anuales_observacion = models.CharField('Observaciones', max_length=250)
    potrero_sin_arboles = models.DecimalField(max_digits=10,decimal_places=2)
    sin_arboles_observacion = models.CharField('Observaciones', max_length=250)
    potrero_arboles = models.DecimalField(max_digits=10,decimal_places=2)
    arboles_observacion = models.CharField('Observaciones', max_length=250)
    plantaciones_forestales = models.DecimalField(max_digits=10,decimal_places=2)
    forestales_observacion = models.CharField('Observaciones', max_length=250)

    class Meta:
        verbose_name= 'Uso de tierra'

SEXO_CHOICE = (
    (1,'Hombres de 25 adelante'),
    (2,'Mujeres de 25 adelante'),
    (3,'Hombres Jóvenes de 15 a 24'),
    (4,'Mujeres Jóvenes de 15 a 24'),
    (5,'Hombres adolescentes de 9 a 14'),
    (6,'Mujeres adolescentes de 9 a 14'),
    (7,'Hombres niños de 1 a 8'),
    (8,'Mujeres niñas de 1 a 8'),
    )

CHOICE_EBA = (
        (1, "Finalizado"),
        (2, "Activo"),

    )

#------------------------------------------------------------------------
#  Modelo: Educacion
#------------------------------------------------------------------------
class Educacion(models.Model):
    sexo_edad = models.IntegerField(choices=SEXO_CHOICE)
    num_persona = models.IntegerField()
    nosabe_leer = models.IntegerField()
    pri_incompleta = models.IntegerField()
    pri_completa = models.IntegerField()
    secu_incompleta = models.IntegerField()
    secu_completa = models.IntegerField()
    uni_o_tecnico = models.IntegerField()
    estudiando = models.IntegerField()
    circ_estudio_adulto = models.IntegerField(choices=CHOICE_EBA)
    

    class Meta:
        ordering = ('sexo_edad',)
        verbose_name_plural = "Educación"

#---------------------------------------------------------------------
#  Modelo: Seguridad alimentaria e ingreso en productos saf
#---------------------------------------------------------------------
SISTEMAS_CHOICES=(
    (1,'Cafe bajo sombra'),(2,'Cacao bajo sombra'),
    (3,'Parcela energetica'),(4,'Parcela silvopastoril'),
    (5,'Cerca Viva'),(6,'Huerto mixto'),(7,'Parcela forrajera'),
    (8,'Parcela frutales'),(9,'Cultivos Anuales con Arboles'),
    (10,'Cultivo callejon'),(11,'Parcela agroforestal succecional'),
    (12,'Achiote con sombra'),(13,'Parcela de coco'),
    (14,'Parcela de pejibaye'),(15,'Parcela con raices'),(16,'Tuberculos'))

UNIDAD_COMER_CHOICES=(
    (1,'qq pergaminos'),(2,'qq'),
    (3,'Unidad'),(4,'Cienes'),
    (5,'Pie tablar'),(6,'Docenas'),
    (7,'Racimo'),(8,'Lbs'),
    (9,'Carga'),(10,'Cabezas')
    )

class SeguridadSaf(models.Model):
    cultivos = models.IntegerField(choices=SISTEMAS_CHOICES)
    area_desarrollo = models.FloatField('Area en desarrollo (en Mz)')
    area_produccion = models.FloatField('Area en producción (en Mz)')
    unidad_medida = models.IntegerField(choices=UNIDAD_COMER_CHOICES)
    produccion_total = models.FloatField()
    auto_consumo = models.FloatField()
    perdidas = models.FloatField('Pérdidas')
    venta_no = models.FloatField('Venta no organizada')
    precio_promedio_no = models.FloatField('Precio promedio')
    venta_organizada = models.FloatField('Venta organizada')
    precio_promedio_orga = models.FloatField('Precio promedio')

    class Meta:
        verbose_name = ('SeguridadSaf')
        verbose_name_plural = ('SeguridadSaf')

#---------------------------------------------------------------------
# Modelo: seguridad cultivos anuales
#---------------------------------------------------------------------

class SeguridadCAnuales(models.Model):
    cultivos = models.IntegerField(choices)
    area_produccion