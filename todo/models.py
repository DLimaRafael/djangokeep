from pyexpat import model
from django import forms
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
