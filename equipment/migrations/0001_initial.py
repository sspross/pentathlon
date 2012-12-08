# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GiantSlalomEquipment'
        db.create_table('equipment_giantslalomequipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('multiplier', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
        ))
        db.send_create_signal('equipment', ['GiantSlalomEquipment'])

        # Adding model 'JumpEquipment'
        db.create_table('equipment_jumpequipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('multiplier', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
        ))
        db.send_create_signal('equipment', ['JumpEquipment'])


    def backwards(self, orm):
        # Deleting model 'GiantSlalomEquipment'
        db.delete_table('equipment_giantslalomequipment')

        # Deleting model 'JumpEquipment'
        db.delete_table('equipment_jumpequipment')


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
        }
    }

    complete_apps = ['equipment']