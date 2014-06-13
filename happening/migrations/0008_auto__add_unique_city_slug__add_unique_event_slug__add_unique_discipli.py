# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'City', fields ['slug']
        db.create_unique('happening_city', ['slug'])

        # Adding unique constraint on 'Event', fields ['slug']
        db.create_unique('happening_event', ['slug'])

        # Adding unique constraint on 'Discipline', fields ['slug']
        db.create_unique('happening_discipline', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Discipline', fields ['slug']
        db.delete_unique('happening_discipline', ['slug'])

        # Removing unique constraint on 'Event', fields ['slug']
        db.delete_unique('happening_event', ['slug'])

        # Removing unique constraint on 'City', fields ['slug']
        db.delete_unique('happening_city', ['slug'])


    models = {
        'happening.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True'})
        },
        'happening.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'happening.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['happening.City']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2550', 'blank': 'True'}),
            'discipline': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['happening.Discipline']"}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_attendees': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'registration_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'starts': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['happening']