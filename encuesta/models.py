# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import *
from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField 

SEXO_PRODUCTOR_CHOICES = (
    (1,'Mujer'),
    (3,'Hombre')
)

class Productores(models.Model):
    nombre = models.CharField('Nombre y apellido', max_length=250, null=True, blank=True)
    cedula_productor = models.CharField(max_length=25,null=True,blank=True,
                                        help_text='Introduzca cedula del productor')
    sexo = models.IntegerField('Sexo del productor', choices=SEXO_PRODUCTOR_CHOICES, 
                                null = True, blank=True)

    class Meta:
        verbose_name= 'Productores'
        verbose_name_plural = 'Productores'

    def __unicode__(self):
        return u'%s ' % (str(self.nombre))

class Recolector(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        unique_together = ('nombre',)

    def __unicode__(self):
        return self.nombre

class Encuesta(models.Model):
    fecha = models.DateField('Fecha de la encuesta', help_text='Introduzca año-mes-dia')
    ano = models.IntegerField('año', editable=False)
    recolector = models.ForeignKey(Recolector, verbose_name='Nombre recolector de datos')
    fecha2 = models.DateField('Fecha de ingreso de la encuesta')
    personas = models.CharField('Personas que introdujeron los datos', max_length=250)
    oficina = models.CharField('Oficina de introducción de datos', max_length=50)

    def __unicode__(self):
        return u'%s - %s' % (str(self.fecha),str(self.recolector))

    def save(self, *args, **kwargs):
        self.ano = self.fecha.year
        super(Encuesta, self).save(*args, **kwargs)

    def __productor__(self):
        campesino = Finca.objects.filter(encuesta__id=self.id)
        return campesino[0]


TIPO_CHOICES = (
    (1,'Casa de madera rolliza con techo de paja'),
    (2,'Casa de madera y techo de paja'),
    (3,'Casa de madera con techo de zinc'),
    (4,'Casa minifalda con techo de zinc'),
    (5,'Casa de concreto con techo de zinc')
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
    nombre_productor = models.ForeignKey('Productores')
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
        return u'%s' % (self.nombre_productor)

    class Meta:
        ordering = ('finca',)
        verbose_name= 'Datos generales de la finca'

#-------------------------------------------------------------
#     uso de la tierra
#-------------------------------------------------------------

class UsoTierra(models.Model):
    bosque_primario = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    primario_observacion = models.CharField('Observaciones', max_length=250)
    bosque_secundario = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    secundario_observacion = models.CharField('Observaciones', max_length=250)
    tacotal =  models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    tacotal_observacion = models.CharField('Observaciones', max_length=250)
    cultivos_perennes = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    perennes_observacion = models.CharField('Observaciones', max_length=250)
    cultivos_semiperennes = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    semiperennes_observacion = models.CharField('Observaciones', max_length=250)
    cultivos_anuales = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    anuales_observacion = models.CharField('Observaciones', max_length=250)
    potrero_sin_arboles = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    sin_arboles_observacion = models.CharField('Observaciones', max_length=250)
    potrero_arboles = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    arboles_observacion = models.CharField('Observaciones', max_length=250)
    plantaciones_forestales = models.DecimalField(max_digits=10,decimal_places=2, default='0.00')
    forestales_observacion = models.CharField('Observaciones', max_length=250)

    encuesta = models.ForeignKey(Encuesta)

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
    
    encuesta = models.ForeignKey(Encuesta)

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

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Seguridad Saf'
        verbose_name_plural = 'Seguridad Saf'

#---------------------------------------------------------------------
# Modelo: seguridad cultivos anuales
#---------------------------------------------------------------------

class SeguridadCAnuales(models.Model):
    cultivos = models.IntegerField(choices=SISTEMAS_CHOICES)
    area_produccion = models.FloatField('Area en producción (en Mz)')
    unidad_medida = models.IntegerField(choices=UNIDAD_COMER_CHOICES)
    produccion = models.FloatField('Producción')
    auto_consumo = models.FloatField('Auto-consumo')
    perdidas = models.FloatField()
    venta_no = models.FloatField('Venta no organizada')
    precio_promedio_no = models.FloatField('Precio promedio')
    venta_organizada = models.FloatField('Venta organizada')
    precio_promedio_orga = models.FloatField('Precio promedio')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Seguridad A. Ingresos en cultivos anuales'
        verbose_name_plural = 'Seguridad A. Ingresos en cultivos anuales'

#---------------------------------------------------------------------
# Modelo: seguridad cultivos anuales
#---------------------------------------------------------------------

CHOICE_ANIAMLES = (
        (1,'Leche'),
        (2,'Crema'),
        (3,'Cuajada/Queso'),
        (4,'Mantequilla'),
        (5,'Bovinas'),
        (6,'Cerdos'),
        (7,'Manteca'),
        (8,'Aves'),
        (9,'Huevos'),
        (10,'Pelibuey'),
        (11,'Embutidos'),
        (12,'Pescado'),
        (13,'Mariscos'),
        (14,'Otros'),
    )

class SeguridadPAnimal(models.Model):
    producto = models.IntegerField(choices=CHOICE_ANIAMLES)
    unidad_medida = models.IntegerField(choices=UNIDAD_COMER_CHOICES)
    area_produccion = models.FloatField('Area en producción (en Mz)')
    produccion = models.FloatField('Producción')
    auto_consumo = models.FloatField('Auto-consumo')
    perdidas = models.FloatField()
    venta_no = models.FloatField('Venta no organizada')
    precio_promedio_no = models.FloatField('Precio promedio')
    venta_organizada = models.FloatField('Venta organizada')
    precio_promedio_orga = models.FloatField('Precio promedio')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Seguridad A. Ingresos en producto animal'
        verbose_name_plural = 'Seguridad A. Ingresos en producto animales'


#---------------------------------------------------------------------
# Modelo: seguridad y productos procesados
#---------------------------------------------------------------------
CHOICE_PRODUCTOS_PROCESADOS = (
        (1,'Aceite de coco,palma'),
        (2,'Vinagres'),
        (3,'Chocolate, cacao polvo'),
        (4,'Café molido'),
        (5,'Harinas(banano,pejib, fruta de pan)'),
        (6,'Encurtidos, salsas'),
        (7,'Pinolillos, pozoles'),
        (8,'Especias molidas(canela, curcuma, achiote)'),
        (9,'Chips(platanitos,hojuela de yuca)'),
        (10,'Jaleas, Mermeladas'),
        (11,'Bebidas(frescos,jugos,agua de coco)'),
        (12,'Pan, reposterias'),
        (13,'Plantas cuales:'),
        (14,'Semillas cuales'),
        (15,'Otros productos procesados'),
    )
CHOICE_MANEJA = (
        (1, "Mujer"),
        (2, "Hombre"),
        (3, "Ambos"),
    )
CHOICE_PLAN_NEGOCIO = (
        (1, "Mujer"),
        (2, "Hombre"),
        (3, "Ambos"),
    )

class SeguridadPProcesados(models.Model):
    producto = models.IntegerField(choices=CHOICE_ANIAMLES)
    unidad_medida = models.IntegerField(choices=UNIDAD_COMER_CHOICES)
    produccion = models.FloatField('Producción')
    auto_consumo = models.FloatField('Auto-consumo')
    perdidas = models.FloatField()
    venta_no = models.FloatField('Venta no organizada')
    precio_promedio_no = models.FloatField('Precio promedio')
    venta_organizada = models.FloatField('Venta organizada')
    maneja = models.IntegerField(choices=CHOICE_MANEJA)
    plan_negocio = models.IntegerField(choices=CHOICE_PLAN_NEGOCIO)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Seguridad A. Ingresos en productos procesados'
        verbose_name_plural = 'Seguridad A. Ingresos en productos procesados'

#---------------------------------------------------------------------
# Modelo: ingreso familiar por servicios y negocios
#---------------------------------------------------------------------

class ServiciosActividades(models.Model):
    nombre = models.CharField('Servicio y actividad', max_length=250)
    unidad = models.CharField('unidad de medida', max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.unidad)

class IngresoServicioNegocio(models.Model):
    servicios = models.ForeignKey(ServiciosActividades)
    cantidad = models.IntegerField('Cantidad de unidades por año')
    precio = models.FloatField('Precio/unidad en C$')
    ingresos = models.FloatField('Ingreso anual en C$')
    maneja = models.IntegerField(choices=CHOICE_MANEJA)
    plan_negocio = models.IntegerField(choices=CHOICE_PLAN_NEGOCIO)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Ingreso familiar por servicios y negocios'
        verbose_name_plural = 'Ingreso familiar por servicios y negocios'

#---------------------------------------------------------------------
# Modelo: seguridad alimentaria: consumo y adquisiciones
#---------------------------------------------------------------------

ALIMENTO_CHOICES=(
    (1,'Agua'),(2,'Maiz'),
    (3,'Frijol'),(4,'Arroz'),
    (5,'Azucar'),(6,'Yuca'),
    (7,'Malanga'),(8,'Quequisque'),
    (9,'Naranjilla'),(10,'Parras'),
    (11,'Cafe'),(12,'Cacao'),
    (13,'Coco'),(14,'Leña'),
    (15,'Guineo'),(16,'Platano'),
    (17,'Madera'),(18,'Naranja'),
    (19,'Aguacate'),(20,'Pejibaye'),
    (21,'Achiote'),(22,'Leche'),
    (23,'Cuajada'),(24,'Queso'),
    (25,'Crema'),(26,'Carne de Res'),
    (27,'Huevos'),(28,'Gallinas'),
    (29,'Carne de Cerdo'),(30,'Pinolillo'),
    (31,'Avena'),(32,'Pescado'),
    (33,'Pan'),(34,'Aceite'),(35,'Manteca'),
    (36,'Papa'),(37,'Cebolla'),(38,'Chiltoma'),(39,'Tomate'))


CONSUMO_CHOICES=((1,'No suficiente'),(2,'Si suficiente'))

class SeguridadAlimentaria(models.Model):
    alimentos = models.IntegerField(choices=ALIMENTO_CHOICES)
    comprar = models.BooleanField()
    porcentaje_compran = models.IntegerField()
    nivel_consumo_suficiente = models.IntegerField(choices=CONSUMO_CHOICES)
    porcentaje_nivel = models.IntegerField()

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Consumo y adquisiciones" 


#---------------------------------------------------------------------
# Modelo: credito
#---------------------------------------------------------------------
class OrganizacionesDanCredito(models.Model):
    nombre = models.CharField('Nombre de la organización', max_length=250)

    def __unicode__(self):
        return self.nombre

class UsoCredito(models.Model):
    nombre = models.CharField('Uso del credito', max_length=250)

    def __unicode__(self):
        return self.nombre

class Credito(models.Model):
    organizacion = models.ForeignKey(OrganizacionesDanCredito, 
                   verbose_name='Con qué organización tiene crédito actualmente?')
    uso = models.ManyToManyField(UsoCredito, verbose_name='Uso del crédito')
    personas = models.IntegerField('Número de personas beneficiarias de la familia')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = 'Creditos'


#---------------------------------------------------------------------
# Modelo: innovaciones
#---------------------------------------------------------------------

class TipoInnovacion(models.Model):
    nombre = models.CharField('Innovación', max_length=250)

    def __unicode__(self):
        return self.nombre

CHOICE_SI_NO = (
        (1, "Si"),
        (2, "No"),
    )

class Innovacion(models.Model):
    innovacion = models.ForeignKey(TipoInnovacion)
    aplica = models.IntegerField(choices=CHOICE_SI_NO)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = 'Innovaciones'

#---------------------------------------------------------------------
# Modelo: innovaciones
#---------------------------------------------------------------------

class Fotos(models.Model):
    nombre = models.CharField(max_length=200,help_text="Nombre de la foto a subir")
    adjunto = ImageField(upload_to="attachments", blank=True, 
                         help_text="Suba su archivo aqui")

    encuesta = models.ForeignKey(Encuesta)

    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL,settings.ATTACHMENT_FOLDER, self.id)

    def get_download_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL,settings.ATTACHMENT_FOLDER, self.nombre)

    class Meta:
        verbose_name_plural = "Subir archivos fotograficos de las familia"

    def __unicode__(self):
        return self.nombre