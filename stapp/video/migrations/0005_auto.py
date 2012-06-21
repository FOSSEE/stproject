# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field vidio_list on 'Module'
        db.delete_table('video_module_vidio_list')

        # Adding M2M table for field video_list on 'Module'
        db.create_table('video_module_video_list', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm['video.module'], null=False)),
            ('video', models.ForeignKey(orm['video.video'], null=False))
        ))
        db.create_unique('video_module_video_list', ['module_id', 'video_id'])


    def backwards(self, orm):
        # Adding M2M table for field vidio_list on 'Module'
        db.create_table('video_module_vidio_list', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm['video.module'], null=False)),
            ('video', models.ForeignKey(orm['video.video'], null=False))
        ))
        db.create_unique('video_module_vidio_list', ['module_id', 'video_id'])

        # Removing M2M table for field video_list on 'Module'
        db.delete_table('video_module_video_list')


    models = {
        'video.module': {
            'Meta': {'object_name': 'Module'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'video_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['video.Video']", 'symmetrical': 'False'})
        },
        'video.video': {
            'Meta': {'object_name': 'Video'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['video']