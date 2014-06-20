# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.creation_date'
        db.add_column('happening_event', 'creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True, default=datetime.datetime(2014, 6, 20, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.last_modified'
        db.add_column('happening_event', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime(2014, 6, 20, 0, 0), auto_now=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.creation_date'
        db.delete_column('happening_event', 'creation_date')

        # Deleting field 'Event.last_modified'
        db.delete_column('happening_event', 'last_modified')


    models = {
        'happening.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'happening.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'happening.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['happening.City']", 'symmetrical': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '2550'}),
            'discipline': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['happening.Discipline']", 'symmetrical': 'False'}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'max_attendees': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'registration_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'starts': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['happening']