from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)
admin.site.register(models.comment)
admin.site.register(models.Location)
admin.site.register(models.Mood)
admin.site.register(models.Post)
