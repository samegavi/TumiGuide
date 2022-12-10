from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

def validate_titlecase(value):
    if value != value.title():
        raise ValidationError("First letter of each word must be uppercase")

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True, validators=[validate_titlecase])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('guide:place_detail', kwargs={'pk': self.pk})
    
class Topic(models.Model):
    title = models.CharField(max_length = 200, null=False, blank=False, unique=True, validators=[validate_titlecase])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("guide:topic_detail", kwargs={"pk": self.pk})

    #def save(self, *args, **kwargs):
        #titlelist = self.title.split()
        #cappedlist = []
        #for word in titlelist:
            #cappedlist.append(word.capitalize())
        #self.title = " ".join(cappedlist)
        #super().save(*args, **kwargs)

class Entry(models.Model):
    place   = models.ForeignKey(Place, on_delete=models.CASCADE)
    topic   = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title   = models.CharField(max_length = 200, null=False, blank=False, validators=[validate_titlecase])
    details = models.TextField(null=False, blank=False)

    def get_absolute_url(self):
        return reverse("guide:entry_detail", kwargs={"pk": self.pk})
    
    