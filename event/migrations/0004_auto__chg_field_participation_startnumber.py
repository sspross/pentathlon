# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Participation.startnumber'
        db.alter_column('event_participation', 'startnumber', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Participation.startnumber'
        db.alter_column('event_participation', 'startnumber', self.gf('django.db.models.fields.IntegerField')(default=None))

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
            'cross_country_time_hundredths': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'cross_country_time_minutes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'cross_country_time_seconds': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'curling_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curling_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curling_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curling_points': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'giant_slalom_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giant_slalom_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giant_slalom_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giant_slalom_equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipment.GiantSlalomEquipment']"}),
            'giant_slalom_time_hundredths': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'giant_slalom_time_minutes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'giant_slalom_time_seconds': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jump_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jump_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jump_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jump_equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipment.JumpEquipment']"}),
            'jump_one_distance': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'jump_two_distance': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participations'", 'to': "orm['event.Player']"}),
            'startnumber': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'swimming_did_not_finish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swimming_did_not_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swimming_disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swimming_time_hundredths': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'swimming_time_minutes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'swimming_time_seconds': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participations'", 'to': "orm['event.Team']"})
        },
        'event.player': {
            'Meta': {'ordering': "('lastname',)", 'object_name': 'Player'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': 'None', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
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