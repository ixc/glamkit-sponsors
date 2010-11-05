# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SponsorshipType'
        db.create_table('sponsors_sponsorshiptype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('singular', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('plural', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
            ('logo_size', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('sponsors', ['SponsorshipType'])

        # Adding model 'Sponsor'
        db.create_table('sponsors_sponsor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blurb', self.gf('markupfields.fields.SmartlinksTextileField')(blank=True)),
            ('aggregate_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsors.SponsorshipType'], null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('sponsors', ['Sponsor'])


    def backwards(self, orm):
        
        # Deleting model 'SponsorshipType'
        db.delete_table('sponsors_sponsorshiptype')

        # Deleting model 'Sponsor'
        db.delete_table('sponsors_sponsor')


    models = {
        'sponsors.sponsor': {
            'Meta': {'ordering': "['aggregate_type__rank', 'rank']", 'object_name': 'Sponsor'},
            'aggregate_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.SponsorshipType']", 'null': 'True', 'blank': 'True'}),
            'blurb': ('markupfields.fields.SmartlinksTextileField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'sponsors.sponsorshiptype': {
            'Meta': {'ordering': "['rank']", 'object_name': 'SponsorshipType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_size': ('django.db.models.fields.IntegerField', [], {}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'singular': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sponsors']
