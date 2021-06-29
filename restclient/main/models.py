from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RestProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    