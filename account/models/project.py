from django.contrib.auth import get_user_model
from django.db import models
from .base import BaseModel
from .user import Manager


class Project(BaseModel):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"
    TERMINATED = "Terminated"
    PROJECT_STATUS_CHOICES = (
        (NOT_STARTED,'Not Started'),
        (IN_PROGRESS,'In Progress'),
        (CLOSED, 'Closed'),
        (TERMINATED,'Terminated')
    )
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, default="")
    status = models.CharField(choices=PROJECT_STATUS_CHOICES, max_length=55)
    start_date = models.DateField(null=True)
    close_date = models.DateField(null=True)
    reporting_manager = models.ForeignKey(to=Manager, related_name="project", on_delete=models.CASCADE)
    bde_manager = models.ForeignKey(to=Manager, related_name="project_set", on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)


# class ProjectAssign(BaseModel):
#     project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
#     assignor = models.ForeignKey(to=Manager, on_delete=models.CASCADE)
#     assignee = models.ForeignKey(to=Developer, on_delete=models.CASCADE)