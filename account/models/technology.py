from django.db import models

from .base import BaseModel
from .developer import Developer

class Technology(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)


class Skill(models.Model):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    REGULAR = "regular"
    EXPERT = "expert"
    LEVEL_CHOICES = (
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (REGULAR, "Regular"),
        (EXPERT, "Expert"),
    )
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVEL_CHOICES, default=BEGINNER, max_length=55)
    communication = models.BooleanField(default=False)
    developer = models.ForeignKey(to=Developer, on_delete=models.CASCADE)
