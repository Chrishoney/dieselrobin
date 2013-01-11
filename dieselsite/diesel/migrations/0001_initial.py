# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Competition'
        db.create_table('diesel_competition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('random_teams', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('team_size', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('diesel', ['Competition'])

        # Adding model 'Player'
        db.create_table('diesel_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('next', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Player'], null=True, blank=True)),
        ))
        db.send_create_signal('diesel', ['Player'])

        # Adding M2M table for field combo_choice on 'Player'
        db.create_table('diesel_player_combo_choice', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['diesel.player'], null=False)),
            ('character', models.ForeignKey(orm['diesel.character'], null=False))
        ))
        db.create_unique('diesel_player_combo_choice', ['player_id', 'character_id'])

        # Adding M2M table for field starting_combo on 'Player'
        db.create_table('diesel_player_starting_combo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['diesel.player'], null=False)),
            ('character', models.ForeignKey(orm['diesel.character'], null=False))
        ))
        db.create_unique('diesel_player_starting_combo', ['player_id', 'character_id'])

        # Adding model 'Team'
        db.create_table('diesel_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('score', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams', to=orm['diesel.Competition'])),
        ))
        db.send_create_signal('diesel', ['Team'])

        # Adding M2M table for field members on 'Team'
        db.create_table('diesel_team_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['diesel.team'], null=False)),
            ('player', models.ForeignKey(orm['diesel.player'], null=False))
        ))
        db.create_unique('diesel_team_members', ['team_id', 'player_id'])

        # Adding model 'Character'
        db.create_table('diesel_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('combo', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('won', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('diesel', ['Character'])

        # Adding model 'Mission'
        db.create_table('diesel_mission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='missions', to=orm['diesel.Character'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('failed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('locations', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tier', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('diesel', ['Mission'])


    def backwards(self, orm):
        # Deleting model 'Competition'
        db.delete_table('diesel_competition')

        # Deleting model 'Player'
        db.delete_table('diesel_player')

        # Removing M2M table for field combo_choice on 'Player'
        db.delete_table('diesel_player_combo_choice')

        # Removing M2M table for field starting_combo on 'Player'
        db.delete_table('diesel_player_starting_combo')

        # Deleting model 'Team'
        db.delete_table('diesel_team')

        # Removing M2M table for field members on 'Team'
        db.delete_table('diesel_team_members')

        # Deleting model 'Character'
        db.delete_table('diesel_character')

        # Deleting model 'Mission'
        db.delete_table('diesel_mission')


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
        'diesel.character': {
            'Meta': {'object_name': 'Character'},
            'combo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'won': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'diesel.competition': {
            'Meta': {'object_name': 'Competition'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'random_teams': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'team_size': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'diesel.mission': {
            'Meta': {'object_name': 'Mission'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'missions'", 'to': "orm['diesel.Character']"}),
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tier': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        'diesel.player': {
            'Meta': {'object_name': 'Player'},
            'combo_choice': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'characters'", 'symmetrical': 'False', 'to': "orm['diesel.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Player']", 'null': 'True', 'blank': 'True'}),
            'starting_combo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diesel.Character']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'diesel.team': {
            'Meta': {'object_name': 'Team'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams'", 'to': "orm['diesel.Competition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diesel.Player']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['diesel']