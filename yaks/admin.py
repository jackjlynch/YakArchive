from django.contrib import admin
from yaks import models

# Register your models here.
admin.site.register(models.YakLocation)
admin.site.register(models.Yak)
admin.site.register(models.Comment)