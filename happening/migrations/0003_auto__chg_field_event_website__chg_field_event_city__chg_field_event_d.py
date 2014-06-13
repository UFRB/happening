# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.website'
        db.alter_column(u'happening_event', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Event.city'
        db.alter_column(u'happening_event', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Event.description'
        db.alter_column(u'happening_event', 'description', self.gf('django.db.models.fields.TextField')(default='', max_length=2550))

        # Changing field 'Event.location'
        db.alter_column(u'happening_event', 'location', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    def backwards(self, orm):

        # Changing field 'Event.website'
        db.alter_column(u'happening_event', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Event.city'
        db.alter_column(u'happening_event', 'city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Event.description'
        db.alter_column(u'happening_event', 'description', self.gf('django.db.models.fields.TextField')(max_length=2550, null=True))

        # Changing field 'Event.location'
        db.alter_column(u'happening_event', 'location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        u'happening.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2550', 'blank': 'True'}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'max_attendees': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'registration_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'registration_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'starts': ('django.db.models.fields.DateTimeField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['happening']