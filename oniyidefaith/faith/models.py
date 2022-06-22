from turtle import title
from django.db import models

class Faith(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

def __str__(self):
    return self.title

