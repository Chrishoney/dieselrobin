# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('dieselrobin_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dieselrobin', ['Team'])

        # Adding model 'Player'
        db.create_table('dieselrobin_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dieselrobin', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('dieselrobin_team')

        # Deleting model 'Player'
        db.delete_table('dieselrobin_player')


    models = {
        'dieselrobin.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dieselrobin.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['dieselrobin']