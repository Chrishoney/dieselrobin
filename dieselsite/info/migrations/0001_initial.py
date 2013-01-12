# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table('info_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=7)),
            ('data', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('info', ['Document'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table('info_document')


    models = {
        'info.document': {
            'Meta': {'object_name': 'Document'},
            'data': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '7'})
        }
    }

    complete_apps = ['info']