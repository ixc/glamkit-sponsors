# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SponsorshipType.display_heading'
        db.add_column('sponsors_sponsorshiptype', 'display_heading', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SponsorshipType.display_heading'
        db.delete_column('sponsors_sponsorshiptype', 'display_heading')


    models = {
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
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
            'Meta': {'object_name': 'SponsorshipType'},
            'display_heading': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_size': ('django.db.models.fields.IntegerField', [], {}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'singular': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sponsors']
