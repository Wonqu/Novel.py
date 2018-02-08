from django.db import models
from novelpy.app.models import Project


class Note(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
