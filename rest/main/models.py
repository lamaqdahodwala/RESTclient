from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    req_url = models.CharField(max_length=100)