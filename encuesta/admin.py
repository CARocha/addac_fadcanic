from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin
from .forms import *
from import_export.admin import ImportExportModelAdmin
from datetime import date


class FincaInline(admin.StackedInline):
    model = Finca
    form = ProductorAdminForm
    extra = 1
    max_num = 1
    min_num = 1
    fieldsets = (
        (None, {
            'fields': ('nombre_productor', ('person','finca',), 
                ('municipio', 'comunidad', 'microcuenca'), 'area_finca', 
                ('zona', 'coordenadas_gps', 'coordenadas_lg' ))
        }),
        ('Numero de animales en la finca', {
            
            'fields': (('animal_bovino', 'animal_equino', 'animal_porcino'), ('animal_aves',
                'animal_caprino'), )
        }),
        ('Datos generales de la propiedad', {
            
            'fields': (('tipo_casa', 'area_casa', 'seneamiento'), ('fuente_agua', 'legalidad',
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
              ('pastos_corte', 'pasto_obsercacion'),
              ('plantaciones_forestales', 'forestales_observacion'),)
    extra = 1
    max_num = 1
    min_num = 1

class EducacionAdmin(admin.TabularInline):
    model = Educacion
    extra = 1

class SeguridadSafAdmin(admin.TabularInline):
    form = FormSeguridadSaf
    model = SeguridadSaf
    fields = ('cultivos','area_desarrollo','area_produccion','produccion_total',
                'auto_consumo','consumo_animal','perdidas','venta_no','precio_promedio_no',
                'venta_organizada','precio_promedio_orga')
    class Media:  
        css = {
            'all': ('css/saf.css',)
        }
    extra = 1

class SeguridadCAnualesAdmin(admin.TabularInline):
    #form = FormSeguridadCAnuales
    model = SeguridadCAnuales
    fields = ('cultivos','area_produccion','produccion','auto_consumo',
                'consumo_animal','perdidas','venta_no','precio_promedio_no',
                'venta_organizada','precio_promedio_orga')
    extra = 1

class SeguridadPAnimalAdmin(admin.TabularInline):
    #form = FormSeguridadPAnimal
    model = SeguridadPAnimal
    extra = 1

class SeguridadPProcesadosAdmin(admin.TabularInline):
    #form = FormSeguridadPProcesados
    model = SeguridadPProcesados
    extra = 1

class IngresoServicioNegocioAdmin(admin.TabularInline):
    #form = FormIngresoServicioNegocio
    model = IngresoServicioNegocio
    extra = 1

class SeguridadAlimentariaAdmin(admin.TabularInline):
    #form = FormSeguridadAlimentaria
    model = SeguridadAlimentaria
    extra = 1

class CreditoAdmin(admin.TabularInline):
    #form = FormCredito
    model = Credito
    extra = 1

class InnovacionAdmin(admin.TabularInline):
    #form = FormInnovacion
    model = Innovacion
    extra = 1

class FotosAdmin(AdminImageMixin, admin.TabularInline):
    model = Fotos
    extra = 1

class EncuestaAdmin(admin.ModelAdmin):
    fields = (('fecha', 'fecha2'),('recolector', 'personas'), 'oficina2')
    inlines = [FincaInline, UsoTierraAdmin, EducacionAdmin, SeguridadSafAdmin,
               SeguridadCAnualesAdmin, SeguridadPAnimalAdmin,
               SeguridadPProcesadosAdmin, IngresoServicioNegocioAdmin, SeguridadAlimentariaAdmin,
               CreditoAdmin, InnovacionAdmin, FotosAdmin ]

    list_display = ('fecha', 'get_productor','recolector','get_municipio','get_comunidad',
                    'get_propietario','get_total_area')
    list_filter = ('ano','finca__municipio__nombre', 'finca__propietario')
    date_hierarchy = 'fecha'
    search_fields = ['finca__nombre_productor__nombre',]


    def get_productor(self, obj):
        return "\n".join([i.nombre_productor.nombre for i in obj.finca_set.all()])
    get_productor.short_description = 'Productor'

    def get_municipio(self, obj):
        return "\n".join([i.municipio.nombre for i in obj.finca_set.all()])
    get_municipio.short_description = 'Municipio'

    def get_comunidad(self, obj):
        return "\n".join([i.comunidad.nombre for i in obj.finca_set.all()])
    get_comunidad.short_description = 'Comunidad'

    def get_propietario(self, obj):
        return "\n".join([i.propietario for i in obj.finca_set.all()])
    get_propietario.short_description = 'Propietario'

    def get_total_area(self, obj):
        return "\n".join([str(i.area_finca) for i in obj.finca_set.all()])
    get_total_area.short_description = 'Total area(Mz)'

    class Media:
        css = {
            'all': ('css/select2.css',)
        }
        js = ('js/select2.js','js/encuestas.js',)

class DecadeBornListFilter(admin.SimpleListFilter):
    title = 'joven o adulto'

    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            ('joven', 'joven'),
            ('adulto', 'adulto'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'joven':
            return queryset.filter(edad__range=(16,25))
        if self.value() == 'adulto':
            return queryset.filter(edad__gte=26)


class ProductorAdmin(ImportExportModelAdmin):
    search_fields = ('nombre', 'cedula_productor')
    list_display = ('id', 'nombre', 'sexo', 'cedula_productor')
    list_display_links = ('id', 'nombre',)
    list_filter = ('sexo','pertenece', DecadeBornListFilter)

    class Media:
        css = {
            'all': ('css/pretty.css','css/chosen.css',)
        }
        js = ('js/jquery.mask.js', 'js/productor.js','js/chosen.jquery.js')

class AlimentosSeguridadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre', 'clasificacion')
    list_filter = ('clasificacion',)

# Register your models here.
admin.site.register(Productores, ProductorAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Recolector)
admin.site.register(Oficinas)
admin.site.register(AlimentosSeguridad, AlimentosSeguridadAdmin)
# 
#admin.site.register(Finca)
admin.site.register(CultivosSaf)
admin.site.register(CultivosAnuales)
admin.site.register(ProductoAnimal)
admin.site.register(ProductoProcesado)
admin.site.register(OrganizacionesDanCredito)
admin.site.register(UsoCredito)
admin.site.register(TipoInnovacion)
admin.site.register(ServiciosActividades)
admin.site.register(TipoFinanciamiento)
