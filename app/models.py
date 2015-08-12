from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Owner(AbstractUser):
    rfid = models.BigIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Vehicle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(Owner, blank=True, null=True, related_name="driven_vehicle")
    in_use = models.BooleanField(default=True)

    def natural_key(self):
        return ((self.name))

    def __unicode__(self):
        return u"{}".format(self.name)


class Position(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    time = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, related_name="position")
