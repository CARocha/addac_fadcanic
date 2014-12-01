# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from lugar.models import *
from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField
from django.db.models import F
from datetime import date

SEXO_PRODUCTOR_CHOICES = (
    (1,'Mujer'),
    (3,'Hombre')
)

CHOICE_ORGANIZACION = (
    (1,'FADCANIC'),
    (2,'ADDAC')
)

CHOICE_ACTIVO = (
    (1,'Activo'),
    (2,'No activo')
)

@python_2_unicode_compatible
class Productores(models.Model):
    nombre = models.CharField('Nombre y apellido', max_length=250, null=True, blank=True)
    cedula_productor = models.CharField(max_length=25,null=True,blank=True,
                                        help_text='Introduzca cedula del productor')
    sexo = models.IntegerField('Sexo del productor', choices=SEXO_PRODUCTOR_CHOICES, 
                                null=True, blank=True)
    celular = models.IntegerField('Número celular', null=True, blank=True)
    nacimiento = models.DateField('Fecha de nacimiento', null=True, blank=True)
    pertenece = models.IntegerField(choices=CHOICE_ORGANIZACION, null=True, blank=True)
    activo = models.IntegerField(choices=CHOICE_ACTIVO, null=True, blank=True)

    contador = models.IntegerField(editable=False)
    edad = models.IntegerField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name= 'Productores'
        verbose_name_plural = 'Productores'


    def __str__(self):
        return u'%s' % (self.nombre)

    def save(self, *args, **kwargs):
        self.contador = 1
        today = date.today()
        try: 
            edad1 = self.nacimiento.replace(year=today.year)
        except ValueError:
            edad1 = self.nacimiento.replace(year=today.year, day=self.nacimiento.day-1)
        if edad1 > today:
            self.edad = today.year - self.nacimiento.year - 1
        else:
            self.edad = today.year - self.nacimiento.year 
        super(Productores, self).save(*args, **kwargs)

class Recolector(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        unique_together = ('nombre',)
        verbose_name_plural = 'Recolectores'

    def __unicode__(self):
        return self.nombre

class Oficinas(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        unique_together = ('nombre',)
        verbose_name_plural = 'Oficinas'

    def __unicode__(self):
        return self.nombre

@python_2_unicode_compatible
class Encuesta(models.Model):
    fecha = models.DateField('Fecha de la encuesta', help_text='Introduzca fecha')
    ano = models.IntegerField('año', editable=False)
    recolector = models.ForeignKey(Recolector, verbose_name='Nombre recolector de datos')
    fecha2 = models.DateField('Fecha de ingreso de la encuesta', null=True, blank=True)
    personas = models.CharField('Personas que introdujeron los datos', max_length=250, null=True,
                                blank=True)
    #oficina = models.ForeignKey(Oficinas, verbose_name='Oficina de introducción de datos',
    #                            null=True, blank=True)
    oficina2 = models.ForeignKey(Oficinas, verbose_name='Oficina de introducción de datos', null=True, blank=True)

    def __str__(self):
        return u'%s - %s' % (str(self.fecha),str(self.recolector))

    def save(self, *args, **kwargs):
        self.ano = self.fecha.year
        super(Encuesta, self).save(*args, **kwargs)

    #def __productor__(self):
    #    campesino = Finca.objects.filter(encuesta__id=self.id)
    #    return campesino[0]


TIPO_CHOICES = (
    (1,'Madera rolliza con techo de paja'),
    (2,'Madera (tablas) y techo de paja'),
    (3,'Madera (tablas) con techo de zinc'),
    (4,'Minifalda con techo de zinc'),
    (5,'Concreto con techo de zinc'),
    (6,'Otras mejoras(2 pisos..)')
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
    (9,'Pozo rustico sin manejo'),
    (10,'Pozo con brocal y bomba'),
    (11,'Agua filtrada y certificada p/consumo'),
    (12,'Agua por tuberia y bombeo eléctrico'),
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
    ('parientes','Parientes'),
    ('otros','Otros(alquiler o posada)')
    )

LETRINA_CHOICES = (
    (1,'Letrina(buen estado)'),
    (2,'Letrina(mal estado)'),
    (3,'Inodoro'),
    (4,'Sumidero'),
    (5,'Letrina seca')
    )

#---------------------------------------------------------------------------
#      Modelo: Datos generales de las familias socias
#---------------------------------------------------------------------------

@python_2_unicode_compatible
class Finca(models.Model):
    nombre_productor = models.ForeignKey('Productores', related_name='productores')
    finca = models.CharField("Nombre Finca",max_length=150,null=True,blank=True,help_text='Introduzca nombre de la finca')
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
        null=True,
        blank=True, 
        chained_field="comunidad",
        chained_model_field="comunidad", 
        show_all=False, 
        auto_choose=True,
    )
    
    area_finca = models.DecimalField(max_digits=10,decimal_places=2,help_text='Introduzca el area de la finca en MZ')
    zona = models.IntegerField(null=True, blank=True)
    coordenadas_gps = models.DecimalField('Coordenadas Latitud',max_digits=8, decimal_places=6 ,null=True,blank=True,help_text='Introduzca las coordenadas Latitud')
    coordenadas_lg = models.DecimalField('Coordenadas Longitud', max_digits=8, decimal_places=6, null=True, blank=True, help_text="Introduzca las coordenadas Longitud")
    animal_bovino = models.IntegerField(help_text='Introduzca cuantos animales bovinos tiene')
    animal_porcino = models.IntegerField(help_text='Introduzca cuantos animales porcinos tiene')
    animal_equino = models.IntegerField(help_text='Introduzca cuantos animales equinos tiene')
    animal_aves = models.IntegerField(help_text='Introduzca cuantas aves tiene')
    animal_caprino = models.IntegerField(help_text='Introduzca cuantos animales caprino o pelibuey tiene')
    tipo_casa = models.IntegerField(max_length=60,choices=TIPO_CHOICES,help_text='Introduzca que tipo de casa tiene')
    area_casa = models.DecimalField(max_digits=10,decimal_places=2,help_text='Introduzca area de la casa en pie cuadrado')
    seneamiento = models.IntegerField(choices=LETRINA_CHOICES)
    fuente_agua = models.IntegerField(max_length=60,choices=AGUA_CHOICES,help_text='Introduzca gestion del agua')
    legalidad = models.IntegerField(max_length=60,choices=LEGALIDAD_CHOICES, help_text='Introduzca la legalidad de la propiedad')
    propietario = models.CharField(max_length=50,choices=DUENO_CHOICES,help_text='Introduzca el propietario de la finca')

    encuesta = models.ForeignKey(Encuesta)

    def __str__(self):
        return u'%s' % (self.nombre_productor)

    def save(self, *args, **kwargs):
        Productores.objects.filter(id=self.nombre_productor_id).update(contador=F('contador') + 1)
        super(Finca, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('finca',)
        verbose_name= 'Datos generales de la finca'

#-------------------------------------------------------------
#     uso de la tierra
#-------------------------------------------------------------

class UsoTierra(models.Model):
    bosque_primario = models.DecimalField(max_digits=10,decimal_places=2, 
                                          default='0.00', null=True, blank=True)
    primario_observacion = models.CharField('Observaciones', max_length=250, 
                                            null=True, blank=True)
    bosque_secundario = models.DecimalField(max_digits=10,decimal_places=2, 
                                            default='0.00', null=True, blank=True)
    secundario_observacion = models.CharField('Observaciones', max_length=250,
                                              null=True, blank=True)
    tacotal =  models.DecimalField(max_digits=10,decimal_places=2, 
                                    default='0.00', null=True, blank=True)
    tacotal_observacion = models.CharField('Observaciones', max_length=250,
                                            null=True, blank=True)
    cultivos_perennes = models.DecimalField(max_digits=10,decimal_places=2, 
                                            default='0.00', null=True, blank=True)
    perennes_observacion = models.CharField('Observaciones', max_length=250,
                                            null=True, blank=True)
    cultivos_semiperennes = models.DecimalField(max_digits=10,decimal_places=2, 
                                                default='0.00', null=True, blank=True)
    semiperennes_observacion = models.CharField('Observaciones', max_length=250,
                                                null=True, blank=True)
    cultivos_anuales = models.DecimalField(max_digits=10,decimal_places=2, 
                                            default='0.00', null=True, blank=True)
    anuales_observacion = models.CharField('Observaciones', max_length=250,
                                            null=True, blank=True)
    potrero_sin_arboles = models.DecimalField(max_digits=10,decimal_places=2, 
                                              default='0.00', null=True, blank=True)
    sin_arboles_observacion = models.CharField('Observaciones', max_length=250,
                                                null=True, blank=True)
    potrero_arboles = models.DecimalField(max_digits=10,decimal_places=2, 
                                        default='0.00', null=True, blank=True)
    arboles_observacion = models.CharField('Observaciones', max_length=250,
                                            null=True, blank=True)
    pastos_corte = models.DecimalField(max_digits=10,decimal_places=2, 
                                                default='0.00', null=True, blank=True)
    pasto_obsercacion = models.CharField('Observaciones', max_length=250, 
                                                null=True, blank=True)
    plantaciones_forestales = models.DecimalField(max_digits=10,decimal_places=2, 
                                                default='0.00', null=True, blank=True)
    forestales_observacion = models.CharField('Observaciones', max_length=250, 
                                                null=True, blank=True)

    total_uso = models.FloatField(editable=False)

    encuesta = models.ForeignKey(Encuesta)

    def save(self, *args, **kwargs):
        self.total_uso = self.bosque_primario + self.bosque_secundario + \
                         self.tacotal + self.cultivos_perennes + \
                         self.cultivos_semiperennes + self.cultivos_anuales + \
                         self.potrero_sin_arboles + self.potrero_arboles + \
                         self.plantaciones_forestales
        super(UsoTierra, self).save(*args, **kwargs)

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
    num_persona = models.IntegerField('No. de persona')
    nosabe_leer = models.IntegerField('No sabe leer')
    pri_incompleta = models.IntegerField('Primaria incompleta')
    pri_completa = models.IntegerField('Primaria completa')
    secu_incompleta = models.IntegerField()
    secu_completa = models.IntegerField()
    uni_o_tecnico = models.IntegerField('técnico')
    estudiando = models.IntegerField('Universitario')
    #circ_estudio_adulto = models.IntegerField(choices=CHOICE_EBA, null=True, blank=True)
    estu_eba = models.IntegerField('Estu. EBA', null=True, blank=True)
    estu_mined = models.IntegerField('Estu. MINED', null=True, blank=True)
    estu_uni = models.IntegerField('Estu. UNV.Tecn', null=True, blank=True)
    egresado_eba = models.IntegerField('Egresado EBA', null=True, blank=True)
    egresado_mined = models.IntegerField('Egresado MINED', null=True, blank=True)

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

@python_2_unicode_compatible
class CultivosSaf(models.Model):
    nombre = models.CharField(max_length=250)
    unidad = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cultivos SAF"

    def __str__(self):
        return '%s - %s' % (self.nombre, self.unidad)

class SeguridadSaf(models.Model):
    cultivos = models.ForeignKey(CultivosSaf)
    area_desarrollo = models.FloatField('Area en desarrollo (en Mz)')
    area_produccion = models.FloatField('Area en producción (en Mz)')
    produccion_total = models.FloatField(null=True, blank=True)
    consumo_animal = models.FloatField(null=True, blank=True)
    auto_consumo = models.FloatField(null=True, blank=True)
    perdidas = models.FloatField('Pérdidas', null=True, blank=True)
    venta_no = models.FloatField('Venta no organizada', null=True, blank=True)
    precio_promedio_no = models.FloatField('Precio promedio/unidad', null=True, blank=True)
    venta_organizada = models.FloatField('Venta organizada', null=True, blank=True)
    precio_promedio_orga = models.FloatField('Precio promedio/unidad', null=True, blank=True)

    rendimiento = models.FloatField(editable=False, null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Seguridad Saf'
        verbose_name_plural = 'Seguridad Saf'

    def save(self, *args, **kwargs):
        self.rendimiento = self.produccion_total / self.area_produccion
        super(SeguridadSaf, self).save(*args, **kwargs)

#---------------------------------------------------------------------
# Modelo: seguridad cultivos anuales
#---------------------------------------------------------------------
@python_2_unicode_compatible
class CultivosAnuales(models.Model):
    nombre = models.CharField(max_length=250)
    unidad = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cultivos anuales"

    def __str__(self):
        return '%s - %s' % (self.nombre, self.unidad)


class SeguridadCAnuales(models.Model):
    cultivos = models.ForeignKey(CultivosAnuales)
    area_produccion = models.FloatField('Area en producción (en Mz)')
    produccion = models.FloatField('Producción total')
    consumo_animal = models.FloatField(null=True, blank=True)
    auto_consumo = models.FloatField('Auto-consumo', null=True, blank=True)
    perdidas = models.FloatField(null=True, blank=True)
    venta_no = models.FloatField('Venta no organizada', null=True, blank=True)
    precio_promedio_no = models.FloatField('Precio promedio', null=True, blank=True)
    venta_organizada = models.FloatField('Venta organizada', null=True, blank=True)
    precio_promedio_orga = models.FloatField('Precio promedio', null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    #class Meta:
    #    verbose_name = 'Seguridad A. Ingresos en cultivos anuales'
    #    verbose_name_plural = 'Seguridad A. Ingresos en cultivos anuales'

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

CHOICE_MANEJA = (
        (1, "Mujer"),
        (2, "Hombre"),
        (3, "Ambos"),
    )
CHOICE_PLAN_NEGOCIO = (
        (1, "Si"),
        (2, "No"),
    )
@python_2_unicode_compatible
class ProductoAnimal(models.Model):
    nombre = models.CharField(max_length=250)
    unidad = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Producto animal"

    def __str__(self):
        return '%s - %s' % (self.nombre, self.unidad)

class SeguridadPAnimal(models.Model):
    producto = models.ForeignKey(ProductoAnimal)
    #unidad_medida = models.IntegerField(choices=UNIDAD_COMER_CHOICES)
    produccion = models.FloatField('Producción')
    auto_consumo = models.FloatField('Auto-consumo')
    perdidas = models.FloatField()
    venta_no = models.FloatField('Venta no organizada')
    precio_promedio_no = models.FloatField('Precio promedio')
    venta_organizada = models.FloatField('Venta organizada')
    precio_promedio_orga = models.FloatField('Precio promedio')
    maneja = models.IntegerField(choices=CHOICE_MANEJA)
    #plan_negocio = models.IntegerField(choices=CHOICE_PLAN_NEGOCIO)

    encuesta = models.ForeignKey(Encuesta)

    #class Meta:
    #    verbose_name = 'Seguridad A. Ingresos en producto animal'
    #    verbose_name_plural = 'Seguridad A. Ingresos en producto animales'


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

@python_2_unicode_compatible
class ProductoProcesado(models.Model):
    nombre = models.CharField(max_length=250)
    unidad = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Producto procesado"

    def __str__(self):
        return '%s - %s' % (self.nombre, self.unidad)

class SeguridadPProcesados(models.Model):
    producto = models.ForeignKey(ProductoProcesado)
    #unidad_medida = models.IntegerField(choices=UNIDAD_COMER_CHOICES)
    produccion = models.FloatField('Producción')
    auto_consumo = models.FloatField('Auto-consumo')
    perdidas = models.FloatField()
    venta_no = models.FloatField('Venta no organizada')
    precio_promedio_no = models.FloatField('Precio promedio')
    venta_organizada = models.FloatField('Venta organizada')
    maneja = models.IntegerField(choices=CHOICE_MANEJA)
    #plan_negocio = models.IntegerField(choices=CHOICE_PLAN_NEGOCIO)

    encuesta = models.ForeignKey(Encuesta)

    #class Meta:
    #    verbose_name = 'Seguridad A. Ingresos en productos procesados'
    #    verbose_name_plural = 'Seguridad A. Ingresos en productos procesados'

#---------------------------------------------------------------------
# Modelo: ingreso familiar por servicios y negocios
#---------------------------------------------------------------------

class ServiciosActividades(models.Model):
    nombre = models.CharField('Servicio y actividad', max_length=250)
    unidad = models.CharField('unidad de medida', max_length=200)

    class Meta:
        verbose_name_plural = "Servicios de actividades"

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

    #class Meta:
    #    verbose_name = 'Ingreso familiar por servicios y negocios'
    #    verbose_name_plural = 'Ingreso familiar por servicios y negocios'

#---------------------------------------------------------------------
# Modelo: seguridad alimentaria: consumo y adquisiciones
#---------------------------------------------------------------------

ALIMENTO_CHOICES=(
    (1,'Agua'),(2,'Maiz'),
    (3,'Frijol'),(4,'Arroz'),
    (5,'Azucar'),(6,'Yuca'),
    (7,'Malanga'),(8,'Quequisque'),
    (9,'Naranjilla'),(10,'Parras'),
    (11,'Café'),(12,'Cacao'),
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

CLASIFICACION_CHOICES=((1,'Carbohidratos'),(2,'Vitaminas'),
                        (3,'Grasas'), (4,'Proteínas'),
                        (5,'Minerales'))

class AlimentosSeguridad(models.Model):
    nombre = models.CharField(max_length=250)
    clasificacion = models.IntegerField(choices=CLASIFICACION_CHOICES)

    def __unicode__(self):
        return self.nombre

CONSUMO_CHOICES=((1,'No suficiente'),(2,'Si suficiente'))
CONSUMO_CHOICES_2=((1,'Diario'),(2,'Semanal'), 
                   (3, 'Ocasional'), (4,'No'))

class SeguridadAlimentaria(models.Model):
    alimentos = models.ForeignKey(AlimentosSeguridad)
    consumo = models.IntegerField(choices=CONSUMO_CHOICES_2)
    comprar = models.BooleanField()
    #porcentaje_compran = models.IntegerField()
    #nivel_consumo_suficiente = models.IntegerField(choices=CONSUMO_CHOICES)
    #porcentaje_nivel = models.IntegerField()

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "S.A. Consumo y adquisiciones" 


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

class TipoFinanciamiento(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

class Credito(models.Model):
    organizacion = models.ForeignKey(OrganizacionesDanCredito, 
                   verbose_name='Con qué organización tiene crédito actualmente?')
    tipo_fina = models.ForeignKey(TipoFinanciamiento)
    uso = models.ManyToManyField(UsoCredito, verbose_name='Rubro/Destino')
    personas = models.IntegerField('Número de personas beneficiarias de la familia')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = 'Creditos'


#---------------------------------------------------------------------
# Modelo: innovaciones
#---------------------------------------------------------------------

class TipoInnovacion(models.Model):
    nombre = models.CharField('Innovación', max_length=250)

    class Meta:
        verbose_name_plural = 'Tipo de innovaciones'

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

    #class Meta:
    #    verbose_name_plural = "Subir archivos fotograficos de las familia"

    def __unicode__(self):
        return self.nombre