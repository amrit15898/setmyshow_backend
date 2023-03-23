from django.db import models

# Create your models here.
class EventPost(models.Model):
    requirements = models.CharField(max_length=200)
    payment = models.CharField(max_length=200)
    description  = models.TextField()
    