# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FotosPortada'
        db.create_table(u'portada_fotosportada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'portada', ['FotosPortada'])


    def backwards(self, orm):
        # Deleting model 'FotosPortada'
        db.delete_table(u'portada_fotosportada')


    models = {
        u'portada.fotosportada': {
            'Meta': {'object_name': 'FotosPortada'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portada']