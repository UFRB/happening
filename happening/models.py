from datetime import datetime, timedelta

from django.db import models


class ActiveManager(models.Manager):
    """Return objects with published=True that ends
    at least one hour after the query time"""

    def get_queryset(self):
        next_hour = datetime.now() + timedelta(hours=1)
        return super(ActiveManager, self).get_queryset() \
            .filter(published=True) \
            .filter(ends__gte=next_hour)


class Event(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=2550, blank=True)
    discipline = models.ManyToManyField('Discipline')
    website = models.URLField(blank=True)
    venue = models.CharField(max_length=255)
    city = models.ManyToManyField('City')
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    max_attendees = models.PositiveSmallIntegerField()
    registration_opens = models.DateTimeField()
    registration_closes = models.DateTimeField()
    published = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveManager()

    def __unicode__(self):
        return self.name


class Discipline(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=2, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.state)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'