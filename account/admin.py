from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Developer)
admin.site.register(models.Manager)
admin.site.register(models.Designation)
admin.site.register(models.Certification)
admin.site.register(models.Technology)
# admin.site.register(models.Skill)
admin.site.register(models.Project)
