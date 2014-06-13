# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Discipline'
        db.create_table(u'happening_discipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'happening', ['Discipline'])

        # Adding M2M table for field discipline on 'Event'
        m2m_table_name = db.shorten_name(u'happening_event_discipline')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'happening.event'], null=False)),
            ('discipline', models.ForeignKey(orm[u'happening.discipline'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'discipline_id'])


    def backwards(self, orm):
        # Deleting model 'Discipline'
        db.delete_table(u'happening_discipline')

        # Removing M2M table for field discipline on 'Event'
        db.delete_table(db.shorten_name(u'happening_event_discipline'))


    models = {
        u'happening.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        u'happening.discipline': {
            'Meta': {'object_name': 'Discipline'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'happening.event': {
            'Meta': {'object_name': 'Event'},
            'city': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['happening.City']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2550', 'blank': 'True'}),
            'discipline': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['happening.Discipline']", 'symmetrical': 'False'}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_attendees': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'registration_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'registration_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'starts': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['happening']