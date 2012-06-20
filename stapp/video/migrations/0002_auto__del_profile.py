# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('video_profile')


    def backwards(self, orm):
        # Adding model 'Profile'
        db.create_table('video_profile', (
            ('institute', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('roll_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('video', ['Profile'])


    models = {
        'video.module': {
            'Meta': {'object_name': 'Module'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'vidio_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['video.Video']", 'symmetrical': 'False'})
        },
        'video.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['video']