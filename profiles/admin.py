from django.contrib import admin
from profiles import models
# Register your models here.

admin.site.register(models.MentorData)
admin.site.register(models.AmbassadorData)
admin.site.register(models.MenteeData)