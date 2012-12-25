# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('diesel_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('score', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('diesel', ['Team'])

        # Adding model 'Player'
        db.create_table('diesel_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='players', to=orm['diesel.Team'])),
        ))
        db.send_create_signal('diesel', ['Player'])

        # Adding model 'Character'
        db.create_table('diesel_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('combo', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='characters', to=orm['diesel.Team'])),
        ))
        db.send_create_signal('diesel', ['Character'])

        # Adding model 'Mission'
        db.create_table('diesel_mission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('diesel', ['Mission'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('diesel_team')

        # Deleting model 'Player'
        db.delete_table('diesel_player')

        # Deleting model 'Character'
        db.delete_table('diesel_character')

        # Deleting model 'Mission'
        db.delete_table('diesel_mission')


    models = {
        'diesel.character': {
            'Meta': {'object_name': 'Character'},
            'combo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['diesel.Team']"})
        },
        'diesel.mission': {
            'Meta': {'object_name': 'Mission'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'diesel.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['diesel.Team']"})
        },
        'diesel.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['diesel']