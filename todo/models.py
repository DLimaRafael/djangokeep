from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    content = models.TextField(blank=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        name = getattr(self, 'content')
        return name[:40]