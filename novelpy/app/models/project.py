from django.db import models
from novelpy.app.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
