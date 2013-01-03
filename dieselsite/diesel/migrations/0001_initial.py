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
            ('max_players', self.gf('django.db.models.fields.PositiveIntegerField')(default=3)),
        ))
        db.send_create_signal('diesel', ['Team'])

        # Adding model 'Player'
        db.create_table('diesel_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='players', to=orm['diesel.Team'])),
            ('completed_missions', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('killed_characters', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('diesel', ['Player'])

        # Adding model 'Character'
        db.create_table('diesel_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('combo', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='characters', to=orm['diesel.Team'])),
            ('chosen_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('alive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('won', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('diesel', ['Character'])

        # Adding model 'RegularMission'
        db.create_table('diesel_regularmission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Player'])),
            ('combo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Character'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('failed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('new_locations', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('diesel', ['RegularMission'])

        # Adding model 'BonusMission'
        db.create_table('diesel_bonusmission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Player'])),
            ('combo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Character'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tier', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('diesel', ['BonusMission'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('diesel_team')

        # Deleting model 'Player'
        db.delete_table('diesel_player')

        # Deleting model 'Character'
        db.delete_table('diesel_character')

        # Deleting model 'RegularMission'
        db.delete_table('diesel_regularmission')

        # Deleting model 'BonusMission'
        db.delete_table('diesel_bonusmission')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'diesel.bonusmission': {
            'Meta': {'object_name': 'BonusMission'},
            'combo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Character']"}),
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Player']"}),
            'tier': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'diesel.character': {
            'Meta': {'object_name': 'Character'},
            'alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'chosen_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'combo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['diesel.Team']"}),
            'won': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'diesel.player': {
            'Meta': {'object_name': 'Player'},
            'completed_missions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'killed_characters': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['diesel.Team']"})
        },
        'diesel.regularmission': {
            'Meta': {'object_name': 'RegularMission'},
            'combo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Character']"}),
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_locations': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Player']"})
        },
        'diesel.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_players': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['diesel']