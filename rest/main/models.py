from django.db import models

# Create your models here.
class Project(models.Model):
    req_url = models.CharField(max_length=100)