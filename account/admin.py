from django.contrib import admin
from .models import Role,User,Project,Rating
# Register your models here.

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Rating)    

