from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Driver(AbstractUser):
    rfid = models.BigIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Scooter(models.Model):
    name = models.CharField(max_length=100)
    #lat = models.FloatField()
    #long = models.FloatField()
    #driver = models.ForeignKey(Driver, blank=True, null=True, related_name="driven_scooter")
    #time = models.DateTimeField(auto_now=True)
    in_use = models.BooleanField(default=False)

    def natural_key(self):
        return (self.name)

    def __unicode__(self):
        return u"{}".format(self.name)


class Position(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    time = models.DateTimeField(auto_now=True)
    scooter = models.ForeignKey(Scooter, related_name="position")


class Trip(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    length = models.FloatField()
    driver = models.ForeignKey(Driver, related_name="driver")
    scooter = models.ForeignKey(Scooter, related_name="scooter")
    #minutes

    def __unicode__(self):
        return u"{}".format(self.start)

    class Meta:
        ordering = ('start',)
