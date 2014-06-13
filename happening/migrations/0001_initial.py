# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'happening_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2550, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('starts', self.gf('django.db.models.fields.DateTimeField')()),
            ('ends', self.gf('django.db.models.fields.DateTimeField')()),
            ('max_attendees', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True)),
            ('registration_opens', self.gf('django.db.models.fields.DateTimeField')()),
            ('registration_closes', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'happening', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'happening_event')


    models = {
        u'happening.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2550', 'null': 'True', 'blank': 'True'}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'max_attendees': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'registration_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'registration_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'starts': ('django.db.models.fields.DateTimeField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['happening']