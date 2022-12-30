from django.db import models
from .base import BaseModel


class Designation(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    abbreviation = models.CharField(max_length=55, blank=True)
