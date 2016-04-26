# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.password'
        db.add_column('disk_user', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'User.email'
        db.add_column('disk_user', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75),
                      keep_default=False)

        # Adding field 'User.update_date'
        db.add_column('disk_user', 'update_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default='a', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.password'
        db.delete_column('disk_user', 'password')

        # Deleting field 'User.email'
        db.delete_column('disk_user', 'email')

        # Deleting field 'User.update_date'
        db.delete_column('disk_user', 'update_date')


    models = {
        'disk.user': {
            'Meta': {'object_name': 'User'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'headimg': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['disk']