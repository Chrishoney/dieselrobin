# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamMember'
        db.create_table('diesel_teammember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Player'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Team'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
        ))
        db.send_create_signal('diesel', ['TeamMember'])

        # Removing M2M table for field players on 'Team'
        db.delete_table('diesel_team_players')

        # Deleting field 'Player.next'
        db.delete_column('diesel_player', 'next_id')

        # Adding field 'Player.preferred_server'
        db.add_column('diesel_player', 'preferred_server',
                      self.gf('django.db.models.fields.CharField')(default='cao', max_length=3),
                      keep_default=False)


        # Changing field 'Player.user'
        db.alter_column('diesel_player', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))
        # Adding unique constraint on 'Player', fields ['user']
        db.create_unique('diesel_player', ['user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Player', fields ['user']
        db.delete_unique('diesel_player', ['user_id'])

        # Deleting model 'TeamMember'
        db.delete_table('diesel_teammember')

        # Adding M2M table for field players on 'Team'
        db.create_table('diesel_team_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['diesel.team'], null=False)),
            ('player', models.ForeignKey(orm['diesel.player'], null=False))
        ))
        db.create_unique('diesel_team_players', ['team_id', 'player_id'])

        # Adding field 'Player.next'
        db.add_column('diesel_player', 'next',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diesel.Player'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Player.preferred_server'
        db.delete_column('diesel_player', 'preferred_server')


        # Changing field 'Player.user'
        db.alter_column('diesel_player', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

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
            'account': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'chosen_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': "orm['diesel.Player']"}),
            'combo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_player': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'starts'", 'null': 'True', 'to': "orm['diesel.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'characters'", 'null': 'True', 'to': "orm['diesel.Team']"}),
            'won': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'diesel.competition': {
            'Meta': {'object_name': 'Competition'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'random_teams': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'team_size': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'})
        },
        'diesel.mission': {
            'Meta': {'object_name': 'Mission'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'missions'", 'to': "orm['diesel.Character']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'missions'", 'to': "orm['diesel.Player']"}),
            'tier': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        'diesel.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferred_server': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'diesel.team': {
            'Meta': {'object_name': 'Team'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams'", 'to': "orm['diesel.Competition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diesel.Player']", 'through': "orm['diesel.TeamMember']", 'symmetrical': 'False'}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'diesel.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Player']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diesel.Team']"})
        }
    }

    complete_apps = ['diesel']