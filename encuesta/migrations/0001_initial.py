# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Productores'
        db.create_table(u'encuesta_productores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('cedula_productor', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('contador', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'encuesta', ['Productores'])

        # Adding model 'Recolector'
        db.create_table(u'encuesta_recolector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'encuesta', ['Recolector'])

        # Adding unique constraint on 'Recolector', fields ['nombre']
        db.create_unique(u'encuesta_recolector', ['nombre'])

        # Adding model 'Encuesta'
        db.create_table(u'encuesta_encuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('recolector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Recolector'])),
            ('fecha2', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('personas', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('oficina', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'encuesta', ['Encuesta'])

        # Adding model 'Finca'
        db.create_table(u'encuesta_finca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_productor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Productores'])),
            ('finca', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'municipio', to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('microcuenca', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Microcuenca'])),
            ('area_finca', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('coordenadas_gps', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=6, blank=True)),
            ('coordenadas_lg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=6, blank=True)),
            ('animal_bovino', self.gf('django.db.models.fields.IntegerField')()),
            ('animal_porcino', self.gf('django.db.models.fields.IntegerField')()),
            ('animal_equino', self.gf('django.db.models.fields.IntegerField')()),
            ('animal_aves', self.gf('django.db.models.fields.IntegerField')()),
            ('animal_caprino', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_casa', self.gf('django.db.models.fields.IntegerField')(max_length=60)),
            ('area_casa', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('fuente_agua', self.gf('django.db.models.fields.IntegerField')(max_length=60)),
            ('legalidad', self.gf('django.db.models.fields.IntegerField')(max_length=60)),
            ('propietario', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Finca'])

        # Adding model 'UsoTierra'
        db.create_table(u'encuesta_usotierra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bosque_primario', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('primario_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('bosque_secundario', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('secundario_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('tacotal', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('tacotal_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('cultivos_perennes', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('perennes_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('cultivos_semiperennes', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('semiperennes_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('cultivos_anuales', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('anuales_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('potrero_sin_arboles', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sin_arboles_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('potrero_arboles', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('arboles_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('plantaciones_forestales', self.gf('django.db.models.fields.DecimalField')(default=u'0.00', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('forestales_observacion', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('total_uso', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['UsoTierra'])

        # Adding model 'Educacion'
        db.create_table(u'encuesta_educacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo_edad', self.gf('django.db.models.fields.IntegerField')()),
            ('num_persona', self.gf('django.db.models.fields.IntegerField')()),
            ('nosabe_leer', self.gf('django.db.models.fields.IntegerField')()),
            ('pri_incompleta', self.gf('django.db.models.fields.IntegerField')()),
            ('pri_completa', self.gf('django.db.models.fields.IntegerField')()),
            ('secu_incompleta', self.gf('django.db.models.fields.IntegerField')()),
            ('secu_completa', self.gf('django.db.models.fields.IntegerField')()),
            ('uni_o_tecnico', self.gf('django.db.models.fields.IntegerField')()),
            ('estudiando', self.gf('django.db.models.fields.IntegerField')()),
            ('circ_estudio_adulto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Educacion'])

        # Adding model 'SeguridadSaf'
        db.create_table(u'encuesta_seguridadsaf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos', self.gf('django.db.models.fields.IntegerField')()),
            ('area_desarrollo', self.gf('django.db.models.fields.FloatField')()),
            ('area_produccion', self.gf('django.db.models.fields.FloatField')()),
            ('unidad_medida', self.gf('django.db.models.fields.IntegerField')()),
            ('produccion_total', self.gf('django.db.models.fields.FloatField')()),
            ('auto_consumo', self.gf('django.db.models.fields.FloatField')()),
            ('perdidas', self.gf('django.db.models.fields.FloatField')()),
            ('venta_no', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_no', self.gf('django.db.models.fields.FloatField')()),
            ('venta_organizada', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_orga', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['SeguridadSaf'])

        # Adding model 'SeguridadCAnuales'
        db.create_table(u'encuesta_seguridadcanuales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos', self.gf('django.db.models.fields.IntegerField')()),
            ('area_produccion', self.gf('django.db.models.fields.FloatField')()),
            ('unidad_medida', self.gf('django.db.models.fields.IntegerField')()),
            ('produccion', self.gf('django.db.models.fields.FloatField')()),
            ('auto_consumo', self.gf('django.db.models.fields.FloatField')()),
            ('perdidas', self.gf('django.db.models.fields.FloatField')()),
            ('venta_no', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_no', self.gf('django.db.models.fields.FloatField')()),
            ('venta_organizada', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_orga', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['SeguridadCAnuales'])

        # Adding model 'SeguridadPAnimal'
        db.create_table(u'encuesta_seguridadpanimal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.IntegerField')()),
            ('unidad_medida', self.gf('django.db.models.fields.IntegerField')()),
            ('produccion', self.gf('django.db.models.fields.FloatField')()),
            ('auto_consumo', self.gf('django.db.models.fields.FloatField')()),
            ('perdidas', self.gf('django.db.models.fields.FloatField')()),
            ('venta_no', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_no', self.gf('django.db.models.fields.FloatField')()),
            ('venta_organizada', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_orga', self.gf('django.db.models.fields.FloatField')()),
            ('maneja', self.gf('django.db.models.fields.IntegerField')()),
            ('plan_negocio', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['SeguridadPAnimal'])

        # Adding model 'SeguridadPProcesados'
        db.create_table(u'encuesta_seguridadpprocesados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.IntegerField')()),
            ('unidad_medida', self.gf('django.db.models.fields.IntegerField')()),
            ('produccion', self.gf('django.db.models.fields.FloatField')()),
            ('auto_consumo', self.gf('django.db.models.fields.FloatField')()),
            ('perdidas', self.gf('django.db.models.fields.FloatField')()),
            ('venta_no', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio_no', self.gf('django.db.models.fields.FloatField')()),
            ('venta_organizada', self.gf('django.db.models.fields.FloatField')()),
            ('maneja', self.gf('django.db.models.fields.IntegerField')()),
            ('plan_negocio', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['SeguridadPProcesados'])

        # Adding model 'ServiciosActividades'
        db.create_table(u'encuesta_serviciosactividades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['ServiciosActividades'])

        # Adding model 'IngresoServicioNegocio'
        db.create_table(u'encuesta_ingresoservicionegocio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicios', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.ServiciosActividades'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('ingresos', self.gf('django.db.models.fields.FloatField')()),
            ('maneja', self.gf('django.db.models.fields.IntegerField')()),
            ('plan_negocio', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['IngresoServicioNegocio'])

        # Adding model 'SeguridadAlimentaria'
        db.create_table(u'encuesta_seguridadalimentaria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alimentos', self.gf('django.db.models.fields.IntegerField')()),
            ('comprar', self.gf('django.db.models.fields.BooleanField')()),
            ('porcentaje_compran', self.gf('django.db.models.fields.IntegerField')()),
            ('nivel_consumo_suficiente', self.gf('django.db.models.fields.IntegerField')()),
            ('porcentaje_nivel', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['SeguridadAlimentaria'])

        # Adding model 'OrganizacionesDanCredito'
        db.create_table(u'encuesta_organizacionesdancredito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'encuesta', ['OrganizacionesDanCredito'])

        # Adding model 'UsoCredito'
        db.create_table(u'encuesta_usocredito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'encuesta', ['UsoCredito'])

        # Adding model 'Credito'
        db.create_table(u'encuesta_credito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.OrganizacionesDanCredito'])),
            ('personas', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Credito'])

        # Adding M2M table for field uso on 'Credito'
        m2m_table_name = db.shorten_name(u'encuesta_credito_uso')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('credito', models.ForeignKey(orm[u'encuesta.credito'], null=False)),
            ('usocredito', models.ForeignKey(orm[u'encuesta.usocredito'], null=False))
        ))
        db.create_unique(m2m_table_name, ['credito_id', 'usocredito_id'])

        # Adding model 'TipoInnovacion'
        db.create_table(u'encuesta_tipoinnovacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'encuesta', ['TipoInnovacion'])

        # Adding model 'Innovacion'
        db.create_table(u'encuesta_innovacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.TipoInnovacion'])),
            ('aplica', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Innovacion'])

        # Adding model 'Fotos'
        db.create_table(u'encuesta_fotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('adjunto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Fotos'])


    def backwards(self, orm):
        # Removing unique constraint on 'Recolector', fields ['nombre']
        db.delete_unique(u'encuesta_recolector', ['nombre'])

        # Deleting model 'Productores'
        db.delete_table(u'encuesta_productores')

        # Deleting model 'Recolector'
        db.delete_table(u'encuesta_recolector')

        # Deleting model 'Encuesta'
        db.delete_table(u'encuesta_encuesta')

        # Deleting model 'Finca'
        db.delete_table(u'encuesta_finca')

        # Deleting model 'UsoTierra'
        db.delete_table(u'encuesta_usotierra')

        # Deleting model 'Educacion'
        db.delete_table(u'encuesta_educacion')

        # Deleting model 'SeguridadSaf'
        db.delete_table(u'encuesta_seguridadsaf')

        # Deleting model 'SeguridadCAnuales'
        db.delete_table(u'encuesta_seguridadcanuales')

        # Deleting model 'SeguridadPAnimal'
        db.delete_table(u'encuesta_seguridadpanimal')

        # Deleting model 'SeguridadPProcesados'
        db.delete_table(u'encuesta_seguridadpprocesados')

        # Deleting model 'ServiciosActividades'
        db.delete_table(u'encuesta_serviciosactividades')

        # Deleting model 'IngresoServicioNegocio'
        db.delete_table(u'encuesta_ingresoservicionegocio')

        # Deleting model 'SeguridadAlimentaria'
        db.delete_table(u'encuesta_seguridadalimentaria')

        # Deleting model 'OrganizacionesDanCredito'
        db.delete_table(u'encuesta_organizacionesdancredito')

        # Deleting model 'UsoCredito'
        db.delete_table(u'encuesta_usocredito')

        # Deleting model 'Credito'
        db.delete_table(u'encuesta_credito')

        # Removing M2M table for field uso on 'Credito'
        db.delete_table(db.shorten_name(u'encuesta_credito_uso'))

        # Deleting model 'TipoInnovacion'
        db.delete_table(u'encuesta_tipoinnovacion')

        # Deleting model 'Innovacion'
        db.delete_table(u'encuesta_innovacion')

        # Deleting model 'Fotos'
        db.delete_table(u'encuesta_fotos')


    models = {
        u'encuesta.credito': {
            'Meta': {'object_name': 'Credito'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.OrganizacionesDanCredito']"}),
            'personas': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['encuesta.UsoCredito']", 'symmetrical': 'False'})
        },
        u'encuesta.educacion': {
            'Meta': {'ordering': "(u'sexo_edad',)", 'object_name': 'Educacion'},
            'circ_estudio_adulto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
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
            'oficina': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
            'microcuenca': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Microcuenca']"}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'municipio'", 'to': u"orm['lugar.Municipio']"}),
            'nombre_productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Productores']"}),
            'propietario': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_casa': ('django.db.models.fields.IntegerField', [], {'max_length': '60'})
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
        u'encuesta.organizacionesdancredito': {
            'Meta': {'object_name': 'OrganizacionesDanCredito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'encuesta.productores': {
            'Meta': {'object_name': 'Productores'},
            'cedula_productor': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'contador': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'encuesta.recolector': {
            'Meta': {'unique_together': "((u'nombre',),)", 'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'encuesta.seguridadalimentaria': {
            'Meta': {'object_name': 'SeguridadAlimentaria'},
            'alimentos': ('django.db.models.fields.IntegerField', [], {}),
            'comprar': ('django.db.models.fields.BooleanField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_consumo_suficiente': ('django.db.models.fields.IntegerField', [], {}),
            'porcentaje_compran': ('django.db.models.fields.IntegerField', [], {}),
            'porcentaje_nivel': ('django.db.models.fields.IntegerField', [], {})
        },
        u'encuesta.seguridadcanuales': {
            'Meta': {'object_name': 'SeguridadCAnuales'},
            'area_produccion': ('django.db.models.fields.FloatField', [], {}),
            'auto_consumo': ('django.db.models.fields.FloatField', [], {}),
            'cultivos': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perdidas': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_orga': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {}),
            'unidad_medida': ('django.db.models.fields.IntegerField', [], {}),
            'venta_no': ('django.db.models.fields.FloatField', [], {}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        u'encuesta.seguridadpanimal': {
            'Meta': {'object_name': 'SeguridadPAnimal'},
            'auto_consumo': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneja': ('django.db.models.fields.IntegerField', [], {}),
            'perdidas': ('django.db.models.fields.FloatField', [], {}),
            'plan_negocio': ('django.db.models.fields.IntegerField', [], {}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_orga': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.IntegerField', [], {}),
            'unidad_medida': ('django.db.models.fields.IntegerField', [], {}),
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
            'plan_negocio': ('django.db.models.fields.IntegerField', [], {}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {}),
            'produccion': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.IntegerField', [], {}),
            'unidad_medida': ('django.db.models.fields.IntegerField', [], {}),
            'venta_no': ('django.db.models.fields.FloatField', [], {}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        u'encuesta.seguridadsaf': {
            'Meta': {'object_name': 'SeguridadSaf'},
            'area_desarrollo': ('django.db.models.fields.FloatField', [], {}),
            'area_produccion': ('django.db.models.fields.FloatField', [], {}),
            'auto_consumo': ('django.db.models.fields.FloatField', [], {}),
            'cultivos': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perdidas': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_no': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio_orga': ('django.db.models.fields.FloatField', [], {}),
            'produccion_total': ('django.db.models.fields.FloatField', [], {}),
            'unidad_medida': ('django.db.models.fields.IntegerField', [], {}),
            'venta_no': ('django.db.models.fields.FloatField', [], {}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        u'encuesta.serviciosactividades': {
            'Meta': {'object_name': 'ServiciosActividades'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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