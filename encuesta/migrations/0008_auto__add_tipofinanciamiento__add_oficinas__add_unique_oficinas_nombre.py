# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoFinanciamiento'
        db.create_table(u'encuesta_tipofinanciamiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'encuesta', ['TipoFinanciamiento'])

        # Adding model 'Oficinas'
        db.create_table(u'encuesta_oficinas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'encuesta', ['Oficinas'])

        # Adding unique constraint on 'Oficinas', fields ['nombre']
        db.create_unique(u'encuesta_oficinas', ['nombre'])

        # Adding model 'AlimentosSeguridad'
        db.create_table(u'encuesta_alimentosseguridad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('clasificacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'encuesta', ['AlimentosSeguridad'])

        # Adding field 'Credito.tipo_fina'
        db.add_column(u'encuesta_credito', 'tipo_fina',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['encuesta.TipoFinanciamiento']),
                      keep_default=False)

        # Adding field 'UsoTierra.pastos_corte'
        db.add_column(u'encuesta_usotierra', 'pastos_corte',
                      self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'UsoTierra.pasto_obsercacion'
        db.add_column(u'encuesta_usotierra', 'pasto_obsercacion',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SeguridadPAnimal.plan_negocio'
        db.delete_column(u'encuesta_seguridadpanimal', 'plan_negocio')

        # Deleting field 'Educacion.circ_estudio_adulto'
        db.delete_column(u'encuesta_educacion', 'circ_estudio_adulto')

        # Adding field 'Educacion.estu_eba'
        db.add_column(u'encuesta_educacion', 'estu_eba',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Educacion.estu_mined'
        db.add_column(u'encuesta_educacion', 'estu_mined',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Educacion.estu_uni'
        db.add_column(u'encuesta_educacion', 'estu_uni',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Educacion.egresado_eba'
        db.add_column(u'encuesta_educacion', 'egresado_eba',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Educacion.egresado_mined'
        db.add_column(u'encuesta_educacion', 'egresado_mined',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SeguridadCAnuales.consumo_animal'
        db.add_column(u'encuesta_seguridadcanuales', 'consumo_animal',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'SeguridadCAnuales.perdidas'
        db.alter_column(u'encuesta_seguridadcanuales', 'perdidas', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadCAnuales.precio_promedio_orga'
        db.alter_column(u'encuesta_seguridadcanuales', 'precio_promedio_orga', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadCAnuales.venta_organizada'
        db.alter_column(u'encuesta_seguridadcanuales', 'venta_organizada', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadCAnuales.venta_no'
        db.alter_column(u'encuesta_seguridadcanuales', 'venta_no', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadCAnuales.precio_promedio_no'
        db.alter_column(u'encuesta_seguridadcanuales', 'precio_promedio_no', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadCAnuales.auto_consumo'
        db.alter_column(u'encuesta_seguridadcanuales', 'auto_consumo', self.gf('django.db.models.fields.FloatField')(null=True))
        # Deleting field 'Encuesta.oficina'
        db.delete_column(u'encuesta_encuesta', 'oficina')

        # Adding field 'Encuesta.oficina2'
        db.add_column(u'encuesta_encuesta', 'oficina2',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Oficinas'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SeguridadAlimentaria.nivel_consumo_suficiente'
        db.delete_column(u'encuesta_seguridadalimentaria', 'nivel_consumo_suficiente')

        # Deleting field 'SeguridadAlimentaria.porcentaje_nivel'
        db.delete_column(u'encuesta_seguridadalimentaria', 'porcentaje_nivel')

        # Deleting field 'SeguridadAlimentaria.porcentaje_compran'
        db.delete_column(u'encuesta_seguridadalimentaria', 'porcentaje_compran')

        # Adding field 'SeguridadAlimentaria.consumo'
        db.add_column(u'encuesta_seguridadalimentaria', 'consumo',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Renaming column for 'SeguridadAlimentaria.alimentos' to match new field type.
        db.rename_column(u'encuesta_seguridadalimentaria', 'alimentos', 'alimentos_id')
        # Changing field 'SeguridadAlimentaria.alimentos'
        db.alter_column(u'encuesta_seguridadalimentaria', 'alimentos_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.AlimentosSeguridad']))
        # Adding index on 'SeguridadAlimentaria', fields ['alimentos']
        db.create_index(u'encuesta_seguridadalimentaria', ['alimentos_id'])

        # Deleting field 'SeguridadPProcesados.plan_negocio'
        db.delete_column(u'encuesta_seguridadpprocesados', 'plan_negocio')

        # Adding field 'Finca.zona'
        db.add_column(u'encuesta_finca', 'zona',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Finca.seneamiento'
        db.add_column(u'encuesta_finca', 'seneamiento',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'Finca.microcuenca'
        db.alter_column(u'encuesta_finca', 'microcuenca_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Microcuenca'], null=True))
        # Adding field 'SeguridadSaf.consumo_animal'
        db.add_column(u'encuesta_seguridadsaf', 'consumo_animal',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'SeguridadSaf.precio_promedio_orga'
        db.alter_column(u'encuesta_seguridadsaf', 'precio_promedio_orga', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadSaf.venta_organizada'
        db.alter_column(u'encuesta_seguridadsaf', 'venta_organizada', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadSaf.venta_no'
        db.alter_column(u'encuesta_seguridadsaf', 'venta_no', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadSaf.precio_promedio_no'
        db.alter_column(u'encuesta_seguridadsaf', 'precio_promedio_no', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadSaf.auto_consumo'
        db.alter_column(u'encuesta_seguridadsaf', 'auto_consumo', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadSaf.perdidas'
        db.alter_column(u'encuesta_seguridadsaf', 'perdidas', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'SeguridadSaf.produccion_total'
        db.alter_column(u'encuesta_seguridadsaf', 'produccion_total', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):
        # Removing index on 'SeguridadAlimentaria', fields ['alimentos']
        db.delete_index(u'encuesta_seguridadalimentaria', ['alimentos_id'])

        # Removing unique constraint on 'Oficinas', fields ['nombre']
        db.delete_unique(u'encuesta_oficinas', ['nombre'])

        # Deleting model 'TipoFinanciamiento'
        db.delete_table(u'encuesta_tipofinanciamiento')

        # Deleting model 'Oficinas'
        db.delete_table(u'encuesta_oficinas')

        # Deleting model 'AlimentosSeguridad'
        db.delete_table(u'encuesta_alimentosseguridad')

        # Deleting field 'Credito.tipo_fina'
        db.delete_column(u'encuesta_credito', 'tipo_fina_id')

        # Deleting field 'UsoTierra.pastos_corte'
        db.delete_column(u'encuesta_usotierra', 'pastos_corte')

        # Deleting field 'UsoTierra.pasto_obsercacion'
        db.delete_column(u'encuesta_usotierra', 'pasto_obsercacion')

        # Adding field 'SeguridadPAnimal.plan_negocio'
        db.add_column(u'encuesta_seguridadpanimal', 'plan_negocio',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Educacion.circ_estudio_adulto'
        db.add_column(u'encuesta_educacion', 'circ_estudio_adulto',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Educacion.estu_eba'
        db.delete_column(u'encuesta_educacion', 'estu_eba')

        # Deleting field 'Educacion.estu_mined'
        db.delete_column(u'encuesta_educacion', 'estu_mined')

        # Deleting field 'Educacion.estu_uni'
        db.delete_column(u'encuesta_educacion', 'estu_uni')

        # Deleting field 'Educacion.egresado_eba'
        db.delete_column(u'encuesta_educacion', 'egresado_eba')

        # Deleting field 'Educacion.egresado_mined'
        db.delete_column(u'encuesta_educacion', 'egresado_mined')

        # Deleting field 'SeguridadCAnuales.consumo_animal'
        db.delete_column(u'encuesta_seguridadcanuales', 'consumo_animal')


        # Changing field 'SeguridadCAnuales.perdidas'
        db.alter_column(u'encuesta_seguridadcanuales', 'perdidas', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadCAnuales.precio_promedio_orga'
        db.alter_column(u'encuesta_seguridadcanuales', 'precio_promedio_orga', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadCAnuales.venta_organizada'
        db.alter_column(u'encuesta_seguridadcanuales', 'venta_organizada', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadCAnuales.venta_no'
        db.alter_column(u'encuesta_seguridadcanuales', 'venta_no', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadCAnuales.precio_promedio_no'
        db.alter_column(u'encuesta_seguridadcanuales', 'precio_promedio_no', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadCAnuales.auto_consumo'
        db.alter_column(u'encuesta_seguridadcanuales', 'auto_consumo', self.gf('django.db.models.fields.FloatField')(default=1))
        # Adding field 'Encuesta.oficina'
        db.add_column(u'encuesta_encuesta', 'oficina',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Encuesta.oficina2'
        db.delete_column(u'encuesta_encuesta', 'oficina2_id')

        # Adding field 'SeguridadAlimentaria.nivel_consumo_suficiente'
        db.add_column(u'encuesta_seguridadalimentaria', 'nivel_consumo_suficiente',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'SeguridadAlimentaria.porcentaje_nivel'
        db.add_column(u'encuesta_seguridadalimentaria', 'porcentaje_nivel',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'SeguridadAlimentaria.porcentaje_compran'
        db.add_column(u'encuesta_seguridadalimentaria', 'porcentaje_compran',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'SeguridadAlimentaria.consumo'
        db.delete_column(u'encuesta_seguridadalimentaria', 'consumo')


        # Renaming column for 'SeguridadAlimentaria.alimentos' to match new field type.
        db.rename_column(u'encuesta_seguridadalimentaria', 'alimentos_id', 'alimentos')
        # Changing field 'SeguridadAlimentaria.alimentos'
        db.alter_column(u'encuesta_seguridadalimentaria', 'alimentos', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'SeguridadPProcesados.plan_negocio'
        db.add_column(u'encuesta_seguridadpprocesados', 'plan_negocio',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'Finca.zona'
        db.delete_column(u'encuesta_finca', 'zona')

        # Deleting field 'Finca.seneamiento'
        db.delete_column(u'encuesta_finca', 'seneamiento')


        # Changing field 'Finca.microcuenca'
        db.alter_column(u'encuesta_finca', 'microcuenca_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(default=1, to=orm['lugar.Microcuenca']))
        # Deleting field 'SeguridadSaf.consumo_animal'
        db.delete_column(u'encuesta_seguridadsaf', 'consumo_animal')


        # Changing field 'SeguridadSaf.precio_promedio_orga'
        db.alter_column(u'encuesta_seguridadsaf', 'precio_promedio_orga', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadSaf.venta_organizada'
        db.alter_column(u'encuesta_seguridadsaf', 'venta_organizada', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadSaf.venta_no'
        db.alter_column(u'encuesta_seguridadsaf', 'venta_no', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadSaf.precio_promedio_no'
        db.alter_column(u'encuesta_seguridadsaf', 'precio_promedio_no', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadSaf.auto_consumo'
        db.alter_column(u'encuesta_seguridadsaf', 'auto_consumo', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadSaf.perdidas'
        db.alter_column(u'encuesta_seguridadsaf', 'perdidas', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'SeguridadSaf.produccion_total'
        db.alter_column(u'encuesta_seguridadsaf', 'produccion_total', self.gf('django.db.models.fields.FloatField')(default=1))

    models = {
        u'encuesta.alimentosseguridad': {
            'Meta': {'object_name': 'AlimentosSeguridad'},
            'clasificacion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'encuesta.credito': {
            'Meta': {'object_name': 'Credito'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.OrganizacionesDanCredito']"}),
            'personas': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_fina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.TipoFinanciamiento']"}),
            'uso': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['encuesta.UsoCredito']", 'symmetrical': 'False'})
        },
        u'encuesta.cultivosanuales': {
            'Meta': {'object_name': 'CultivosAnuales'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.cultivossaf': {
            'Meta': {'object_name': 'CultivosSaf'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.educacion': {
            'Meta': {'ordering': "(u'sexo_edad',)", 'object_name': 'Educacion'},
            'egresado_eba': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'egresado_mined': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'estu_eba': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'estu_mined': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'estu_uni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'estudiando': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nosabe_leer': ('django.db.models.fields.IntegerField', [], {}),
            'num_persona': ('django.db.models.fields.IntegerField', [], {}),
            'pri_completa': ('django.db.models.fields.IntegerField', [], {}),
            'pri_incompleta': ('django.db.models.fields.IntegerField', [], {}),
            'secu_completa': ('django.db.models.fields.IntegerField', [], {}),
            'secu_incompleta': ('django.db.models.fields.IntegerField', [], {}),
            'sexo_edad': ('django.db.models.fields.IntegerField', [], {}),
            'uni_o_tecnico': ('django.db.models.fields.IntegerField', [], {})
        },
        u'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fecha2': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oficina2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Oficinas']", 'null': 'True', 'blank': 'True'}),
            'personas': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Recolector']"})
        },
        u'encuesta.finca': {
            'Meta': {'ordering': "(u'finca',)", 'object_name': 'Finca'},
            'animal_aves': ('django.db.models.fields.IntegerField', [], {}),
            'animal_bovino': ('django.db.models.fields.IntegerField', [], {}),
            'animal_caprino': ('django.db.models.fields.IntegerField', [], {}),
            'animal_equino': ('django.db.models.fields.IntegerField', [], {}),
            'animal_porcino': ('django.db.models.fields.IntegerField', [], {}),
            'area_casa': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'area_finca': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'coordenadas_gps': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '6', 'blank': 'True'}),
            'coordenadas_lg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '6', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'fuente_agua': ('django.db.models.fields.IntegerField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legalidad': ('django.db.models.fields.IntegerField', [], {'max_length': '60'}),
            'microcuenca': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Microcuenca']", 'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'municipio'", 'to': u"orm['lugar.Municipio']"}),
            'nombre_productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'productores'", 'to': u"orm['encuesta.Productores']"}),
            'propietario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seneamiento': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_casa': ('django.db.models.fields.IntegerField', [], {'max_length': '60'}),
            'zona': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'encuesta.fotos': {
            'Meta': {'object_name': 'Fotos'},
            'adjunto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.ingresoservicionegocio': {
            'Meta': {'object_name': 'IngresoServicioNegocio'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos': ('django.db.models.fields.FloatField', [], {}),
            'maneja': ('django.db.models.fields.IntegerField', [], {}),
            'plan_negocio': ('django.db.models.fields.IntegerField', [], {}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'servicios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.ServiciosActividades']"})
        },
        u'encuesta.innovacion': {
            'Meta': {'object_name': 'Innovacion'},
            'aplica': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.TipoInnovacion']"})
        },
        u'encuesta.oficinas': {
            'Meta': {'unique_together': "((u'nombre',),)", 'object_name': 'Oficinas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.organizacionesdancredito': {
            'Meta': {'object_name': 'OrganizacionesDanCredito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'encuesta.productoanimal': {
            'Meta': {'object_name': 'ProductoAnimal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.productoprocesado': {
            'Meta': {'object_name': 'ProductoProcesado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.productores': {
            'Meta': {'object_name': 'Productores'},
            'activo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cedula_productor': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'contador': ('django.db.models.fields.IntegerField', [], {}),
            'edad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'pertenece': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'encuesta.recolector': {
            'Meta': {'unique_together': "((u'nombre',),)", 'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.seguridadalimentaria': {
            'Meta': {'object_name': 'SeguridadAlimentaria'},
            'alimentos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.AlimentosSeguridad']"}),
            'comprar': ('django.db.models.fields.BooleanField', [], {}),
            'consumo': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'encuesta.seguridadcanuales': {
            'Meta': {'object_name': 'SeguridadCAnuales'},
            'area_produccion': ('django.db.models.fields.FloatField', [], {}),
            'auto_consumo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'consumo_animal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.CultivosAnuales']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perdidas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_promedio_orga': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'produccion': ('django.db.models.fields.FloatField', [], {}),
            'venta_no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'encuesta.seguridadpanimal': {
            'Meta': {'object_name': 'SeguridadPAnimal'},
            'auto_consumo': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneja': ('django.db.models.fields.IntegerField', [], {}),
            'perdidas': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_orga': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.ProductoAnimal']"}),
            'venta_no': ('django.db.models.fields.FloatField', [], {}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        u'encuesta.seguridadpprocesados': {
            'Meta': {'object_name': 'SeguridadPProcesados'},
            'auto_consumo': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneja': ('django.db.models.fields.IntegerField', [], {}),
            'perdidas': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.ProductoProcesado']"}),
            'venta_no': ('django.db.models.fields.FloatField', [], {}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        u'encuesta.seguridadsaf': {
            'Meta': {'object_name': 'SeguridadSaf'},
            'area_desarrollo': ('django.db.models.fields.FloatField', [], {}),
            'area_produccion': ('django.db.models.fields.FloatField', [], {}),
            'auto_consumo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'consumo_animal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.CultivosSaf']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perdidas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_promedio_orga': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'produccion_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rendimiento': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'venta_no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'encuesta.serviciosactividades': {
            'Meta': {'object_name': 'ServiciosActividades'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.tipofinanciamiento': {
            'Meta': {'object_name': 'TipoFinanciamiento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'encuesta.tipoinnovacion': {
            'Meta': {'object_name': 'TipoInnovacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'encuesta.usocredito': {
            'Meta': {'object_name': 'UsoCredito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'encuesta.usotierra': {
            'Meta': {'object_name': 'UsoTierra'},
            'anuales_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'arboles_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'bosque_primario': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'bosque_secundario': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'cultivos_anuales': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'cultivos_perennes': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'cultivos_semiperennes': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'forestales_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pasto_obsercacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'pastos_corte': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'perennes_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'plantaciones_forestales': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'potrero_arboles': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'potrero_sin_arboles': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'primario_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'secundario_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'semiperennes_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sin_arboles_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tacotal': ('django.db.models.fields.DecimalField', [], {'default': "u'0.00'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'tacotal_observacion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'total_uso': ('django.db.models.fields.FloatField', [], {})
        },
        u'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.microcuenca': {
            'Meta': {'object_name': 'Microcuenca'},
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Comunidad']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'lugar.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['encuesta']