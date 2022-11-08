from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


status_choices = (
('Working' , 'Working'),
('Available' , 'Available'),
('Partial Available' , 'Partial Available'),
('Training' , 'Training'),
)


technologies_known = (
('Python' , 'Python'),
('ROR' , 'ROR'), 
('Node' , 'Node'),
('AngularJS' , 'AngularJS'),
('React' , 'React'),
('PHP' , 'PHP'),
('Android' , 'Android'),
('IOS' , 'IOS'),
('BlockChain' , 'BlockChain'),
('AI-ML' , 'AI-ML'),
('.NET' , '.NET'),
('ReactNative' , 'ReactNative'),

)


class Role(models.Model):  
    name = models.CharField(max_length=50)
    permission = models.TextField(max_length=150)  

    def __str__(self):
        return self.name
class User(AbstractUser):
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length = 15, verbose_name = "Mobile No." )
    designation = models.CharField(max_length = 45, verbose_name = "Designation")
    profile_picture = models.ImageField(upload_to="profile_pic")
    certifications = models.FileField(upload_to = "certifications")
    status = models.CharField(choices = status_choices, default = 'Select Status', max_length = 30 )
    technologies = models.CharField(choices = technologies_known, default = 'Select Technology',  max_length = 35)
    rating=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __obj__(self):
        return self.role
class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="create")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="update" ,null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)   
    
    class Meta:
        abstract = True


class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name=models.CharField(max_length=100)
    
    
    def __obj__(self):
        return self.project_name
   