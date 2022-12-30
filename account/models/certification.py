from django.db import models
from .base import BaseModel
from .developer import Developer


class Certification(BaseModel):
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to = "certifications",blank=True,null=True)
    developer = models.ForeignKey(to=Developer, on_delete=models.CASCADE)
