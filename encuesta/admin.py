from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin

class FincaInline(admin.StackedInline):
    model = Finca
    extra = 1
    max_num = 1
    min_num = 1
    fieldsets = (
        (None, {
            'fields': ('nombre_productor', ('sexo', 'cedula_productor', 'finca'), 
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
    

class UsoTierraAdmin(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = 1
    min_num = 1

class EducacionAdmin(admin.TabularInline):
    model = Educacion
    extra = 1
    max_num = 1
    min_num = 1

class SeguridadSafAdmin(admin.TabularInline):
    model = SeguridadSaf
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
    inlines = [FincaInline, UsoTierraAdmin, EducacionAdmin, SeguridadSafAdmin,
               SeguridadCAnualesAdmin, SeguridadCAnualesAdmin, SeguridadPAnimalAdmin,
               SeguridadPProcesadosAdmin, IngresoServicioNegocioAdmin, SeguridadAlimentariaAdmin,
               CreditoAdmin, InnovacionAdmin, FotosAdmin ]

    list_display = ('fecha', 'recolector', 'oficina')

    # class Media:
    #     js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js', 
    #           'js/select2.js', 'js/select2_locale_es.js', 'js/my_customjs.js',)    
    #     css = {
    #          'all': ('css/select2.css',)
    #     }

# Register your models here.
admin.site.register(Productores)
admin.site.register(Encuesta, EncuestaAdmin)
#admin.site.register(Finca)