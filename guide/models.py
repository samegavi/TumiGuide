from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length = 200)

class Topic(models.Model):
    title = models.CharField(max_length = 200)