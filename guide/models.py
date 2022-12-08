from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length = 200)

class Topic(models.Model):
    title = models.CharField(max_length = 200)

class Entry(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    