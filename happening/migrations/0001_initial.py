# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('happening_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, max_length=2550)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('starts', self.gf('django.db.models.fields.DateTimeField')()),
            ('ends', self.gf('django.db.models.fields.DateTimeField')()),
            ('max_attendees', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('registration_opens', self.gf('django.db.models.fields.DateTimeField')()),
            ('registration_closes', self.gf('django.db.models.fields.DateTimeField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('happening', ['Event'])

        # Adding M2M table for field discipline on 'Event'
        m2m_table_name = db.shorten_name('happening_event_discipline')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['happening.event'], null=False)),
            ('discipline', models.ForeignKey(orm['happening.discipline'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'discipline_id'])

        # Adding M2M table for field city on 'Event'
        m2m_table_name = db.shorten_name('happening_event_city')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['happening.event'], null=False)),
            ('city', models.ForeignKey(orm['happening.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'city_id'])

        # Adding model 'Discipline'
        db.create_table('happening_discipline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('happening', ['Discipline'])

        # Adding model 'City'
        db.create_table('happening_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('happening', ['City'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('happening_event')

        # Removing M2M table for field discipline on 'Event'
        db.delete_table(db.shorten_name('happening_event_discipline'))

        # Removing M2M table for field city on 'Event'
        db.delete_table(db.shorten_name('happening_event_city'))

        # Deleting model 'Discipline'
        db.delete_table('happening_discipline')

        # Deleting model 'City'
        db.delete_table('happening_city')


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
            'city': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['happening.City']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '2550'}),
            'discipline': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['happening.Discipline']"}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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