from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin
from .forms import ProductorAdminForm


class FincaInline(admin.StackedInline):
    model = Finca
    form = ProductorAdminForm
    extra = 1
    max_num = 1
    min_num = 1
    fieldsets = (
        (None, {
            'fields': ('nombre_productor', ('finca'), 
                ('municipio', 'comunidad', 'microcuenca'), 'area_finca', 
                ('coordenadas_gps', 'coordenadas_lg' ))
        }),
        ('Numero de animales en la finca', {
            
            'fields': (('animal_bovino', 'animal_equino', 'animal_porcino'), ('animal_aves',
                'animal_caprino'), )
        }),
        ('Datos generales de la propiedad', {
            
            'fields': (('tipo_casa', 'area_casa'), ('fuente_agua', 'legalidad',
                'propietario'), )
        }),
    )
    

class UsoTierraAdmin(admin.StackedInline):
    model = UsoTierra
    fields = (('bosque_primario','primario_observacion'),
              ('bosque_secundario', 'secundario_observacion'),
              ('tacotal', 'tacotal_observacion'),
              ('cultivos_perennes', 'perennes_observacion'),
              ('cultivos_semiperennes', 'semiperennes_observacion'),
              ('cultivos_anuales', 'anuales_observacion'),
              ('potrero_sin_arboles', 'sin_arboles_observacion'),
              ('potrero_arboles', 'arboles_observacion'),
              ('plantaciones_forestales', 'forestales_observacion'),)
    extra = 1
    max_num = 1
    min_num = 1

class EducacionAdmin(admin.TabularInline):
    model = Educacion
    extra = 1

class SeguridadSafAdmin(admin.TabularInline):
    model = SeguridadSaf
    class Media:  
        css = {
            'all': ('css/saf.css',)
        }
    extra = 1

class SeguridadCAnualesAdmin(admin.TabularInline):
    model = SeguridadCAnuales
    extra = 1

class SeguridadPAnimalAdmin(admin.TabularInline):
    model = SeguridadPAnimal
    extra = 1

class SeguridadPProcesadosAdmin(admin.TabularInline):
    model = SeguridadPProcesados
    extra = 1

class IngresoServicioNegocioAdmin(admin.TabularInline):
    model = IngresoServicioNegocio
    extra = 1

class SeguridadAlimentariaAdmin(admin.TabularInline):
    model = SeguridadAlimentaria
    extra = 1

class CreditoAdmin(admin.TabularInline):
    model = Credito
    extra = 1

class InnovacionAdmin(admin.TabularInline):
    model = Innovacion
    extra = 1

class FotosAdmin(AdminImageMixin, admin.TabularInline):
    model = Fotos
    extra = 1

class EncuestaAdmin(admin.ModelAdmin):
    fields = (('fecha', 'fecha2'),('recolector', 'personas'), 'oficina')
    inlines = [FincaInline, UsoTierraAdmin, EducacionAdmin, SeguridadSafAdmin,
               SeguridadCAnualesAdmin, SeguridadPAnimalAdmin,
               SeguridadPProcesadosAdmin, IngresoServicioNegocioAdmin, SeguridadAlimentariaAdmin,
               CreditoAdmin, InnovacionAdmin, FotosAdmin ]

    list_display = ('fecha','recolector', 'oficina', )

class ProductorAdmin(admin.ModelAdmin):
    search = ('nombre', 'cedula_productor')
    list_display = ('nombre', 'sexo', 'cedula_productor')
    list_filter = ('sexo',)


# Register your models here.
admin.site.register(Productores, ProductorAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Recolector)
# 
admin.site.register(Finca)
admin.site.register(OrganizacionesDanCredito)
admin.site.register(UsoCredito)
admin.site.register(TipoInnovacion)
admin.site.register(ServiciosActividades)