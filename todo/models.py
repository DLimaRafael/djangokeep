from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    content = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)

    
