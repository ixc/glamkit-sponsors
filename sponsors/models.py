from django.db import models
from markupfields.fields import SmartlinksTextileField
from django.conf import settings
import os

UPLOAD_PATH = getattr(settings, 'SPONSORLOGO_UPLOAD_PATH', 'uploads/')
IMAGE_MEDIUM_SCALE = getattr(settings, 'SPONSORLOGO_IMAGE_MEDIUM_SCALE', .9)
IMAGE_SCALE_SCALE = getattr(settings, 'SPONSORLOGO_IMAGE_SCALE_SCALE', .8)

LOGO_SIZE     = (
    (1, 'large'),
    (2, 'medium'),
    (3, 'small'),
)

class SponsorshipType(models.Model):
    singular = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)
    rank = models.IntegerField()
    logo_size = models.IntegerField(choices=LOGO_SIZE)

    class Meta:
        ordering = ['rank']
    
    def __unicode__(self):
        return self.singular

class Sponsor(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Used for alt text if full name is blank.")
    full_name = models.CharField(max_length=200, help_text="Used for alt text.", blank=True)
    slug = models.SlugField()
    blurb = SmartlinksTextileField(blank=True)
    aggregate_type = models.ForeignKey(SponsorshipType, verbose_name="Display on Sponsors' Page as", blank=True, null=True)
    rank = models.IntegerField()
    logo = models.ImageField(upload_to=os.path.join(settings.UPLOAD_PATH, "images/%Y/%m/%d/"), help_text="png file please")
    link = models.URLField()
    
    def canonical_logo(self):
#         print "size", self.aggregate_type.logo_size
        return {
            1: self.large(),
            2: self.medium(),
            3: self.small(),
        }[self.aggregate_type.logo_size]

    def __unicode__(self):
        return self.name
        
    def large(self):
        return self.logo.width, self.logo.height
        
    def medium(self):
        return int(self.logo.width * IMAGE_MEDIUM_SCALE) , int(self.logo.height * IMAGE_MEDIUM_SCALE)

    def small(self):
        return int(self.logo.width * IMAGE_SCALE_SCALE) , int(self.logo.height * IMAGE_SCALE_SCALE)
        
    def alt_text(self):
        return self.full_name or self.name

    class Meta:
        ordering = ['aggregate_type__rank', 'rank']

class SponsorRelationshipBase(models.Model):
    sponsor = models.ForeignKey(Sponsor)
    sponsortype = models.ForeignKey(SponsorshipType, verbose_name="Type")
    annotation = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True
        
    def __unicode__(self):
        return u"%s - %s" % (self.sponsortype, self.sponsor)

    def logosize(self):
        return {
            1: self.sponsor.large(),
            2: self.sponsor.medium(),
            3: self.sponsor.small(),
        }[self.sponsortype.logo_size]
