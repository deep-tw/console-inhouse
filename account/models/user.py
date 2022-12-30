from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    DEVELOPER = "developer"
    MANAGER = "manager"
    ADMIN = "admin"
    ROLES = ((DEVELOPER, "Developer"), (MANAGER, "Manager"), (ADMIN, "Admin"))
    dob = models.DateField(blank=True, null=True, verbose_name="Date of birth")
    phone_number = PhoneNumberField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pic", blank=True, null=True)
    role = models.CharField(choices=ROLES, blank=False, max_length=55)

    def __str__(self) -> str:
        return self.email or self.username

class Manager(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

