from django.db import models
from .user import User

from .designation import Designation


class Developer(models.Model):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    PARTIAL_AVAILABLE = "partial_available"
    TRAINING = "training"
    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable"),
        (PARTIAL_AVAILABLE, "Partial Available"),
        (TRAINING, "Training"),
    )
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    designation = models.ForeignKey(
        to=Designation, on_delete=models.SET_NULL, null=True
    )
    experience = models.FloatField(default=0.0)
    status = models.CharField(choices=STATUS_CHOICES, default=AVAILABLE, max_length=55)
