from django.contrib import admin
from .models import Role,User,Project,Rating,ManagerModel,ProjectAssign
# Register your models here.

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Rating)    
admin.site.register(ProjectAssign)
admin.site.register(ManagerModel)
