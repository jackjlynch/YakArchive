from django.db import models

# Create your models here.
class Yak(models.Model):
    poster_id = models.CharField(max_length=13)
    hide_pin = models.BooleanField()
    message_id = models.CharField(max_length=31)
    longitude = models.FloatField()
    latitude = models.FloatField()
    likes = models.IntegerField()
    message = models.CharField(max_length=200)
    reyaked = models.BooleanField()
    handle = models.CharField(max_length=15, blank=True)

    yaklocation = models.ForeignKey('YakLocation')
    rawdata = models.TextField()

class YakLocation(models.Model):
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()