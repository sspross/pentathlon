# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('event_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('event', ['Event'])

        # Adding model 'Team'
        db.create_table('event_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams', to=orm['event.Event'])),
        ))
        db.send_create_signal('event', ['Team'])

        # Adding model 'Player'
        db.create_table('event_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gender', self.gf('django.db.models.fields.IntegerField')()),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('event', ['Player'])

        # Adding model 'Participation'
        db.create_table('event_participation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participations', to=orm['event.Player'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participations', to=orm['event.Team'])),
            ('startnumber', self.gf('django.db.models.fields.IntegerField')()),
            ('giant_slalom_equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipment.GiantSlalomEquipment'])),
            ('giant_slalom_time', self.gf('django.db.models.fields.TimeField')()),
            ('giant_slalom_did_not_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('giant_slalom_did_not_finish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('giant_slalom_disqualified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('jump_equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipment.JumpEquipment'])),
            ('jump_one_distance', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('jump_two_distance', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('jump_did_not_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('jump_did_not_finish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('jump_disqualified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cross_country_time', self.gf('django.db.models.fields.TimeField')()),
            ('cross_country_did_not_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cross_country_did_not_finish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cross_country_disqualified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('swimming_time', self.gf('django.db.models.fields.TimeField')()),
            ('swimming_did_not_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('swimming_did_not_finish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('swimming_disqualified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('curling_points', self.gf('django.db.models.fields.IntegerField')()),
            ('curling_did_not_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('curling_did_not_finish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('curling_disqualified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('event', ['Participation'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('event_event')

        # Deleting model 'Team'
        db.delete_table('event_team')

        # Deleting model 'Player'
        db.delete_table('event_player')

        # Deleting model 'Participation'
        db.delete_table('event_participation')


    models = {
        'equipment.giantslalomequipment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'GiantSlalomEquipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiplier': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'equipment.jumpequipment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'JumpEquipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiplier': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'event.event': {
            'Meta': {'ordering': "('start_date',)", 'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'event.participation': {
            'Meta': {'ordering': "('startnumber',)", 'object_name': 'Participation'},
            'cross_country_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cross_country_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cross_country_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cross_country_time': ('django.db.models.fields.TimeField', [], {}),
            'curling_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curling_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curling_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curling_points': ('django.db.models.fields.IntegerField', [], {}),
            'giant_slalom_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giant_slalom_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giant_slalom_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giant_slalom_equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipment.GiantSlalomEquipment']"}),
            'giant_slalom_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jump_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jump_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jump_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jump_equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipment.JumpEquipment']"}),
            'jump_one_distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'jump_two_distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participations'", 'to': "orm['event.Player']"}),
            'startnumber': ('django.db.models.fields.IntegerField', [], {}),
            'swimming_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swimming_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swimming_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swimming_time': ('django.db.models.fields.TimeField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participations'", 'to': "orm['event.Team']"})
        },
        'event.player': {
            'Meta': {'object_name': 'Player'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'event.team': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Team'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams'", 'to': "orm['event.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['event']