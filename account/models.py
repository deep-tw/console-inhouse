from django.db import models
from django.contrib.auth.models import AbstractUser



class Role(models.Model):  
    name = models.CharField(max_length=50)
    permission = models.TextField(max_length=150)  

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    
class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)   
    
    class Meta:
        abstract = True

class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
      
   