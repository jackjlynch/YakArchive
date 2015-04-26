from django.db import models

# Create your models here.
class Yak(models.Model):
    poster_id = models.TextField()
    hide_pin = models.BooleanField()
    message_id = models.TextField(primary_key=True)
    delivery_id = models.TextField(blank=True)
    comments = models.IntegerField()
    time = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    likes = models.IntegerField()
    message = models.TextField()
    reyaked = models.BooleanField()
    handle = models.TextField(blank=True, null=True)
    type = models.TextField()


    yaklocation = models.ForeignKey('YakLocation')

class Comment(models.Model):
    message_id = models.TextField()
    comment_id = models.TextField(primary_key=True)
    comment = models.TextField()
    time = models.TextField()
    likes = models.IntegerField()
    poster_id = models.TextField()

class YakLocation(models.Model):
    name = models.TextField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name