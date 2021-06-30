from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    request_url = models.URLField(max_length=100)
    project_name = models.CharField(max_length=100)