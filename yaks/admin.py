from django.contrib import admin
from yaks import models

# Register your models here.
admin.site.register(models.YakLocation)
admin.site.register(models.Comment)

class YakAdmin(admin.ModelAdmin):
    list_display = ('message', 'time', 'poster_id')

admin.site.register(models.Yak, YakAdmin)