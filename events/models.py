from django.db import models

# Create your models here.
requirements_items = (("full band", "full band"), ("two piece", "two piece"), ("single artist", "single artist"), ("acoustic","acoustic" ))
class EventPost(models.Model):
    event_detail = models.TextField()
    requirements = models.CharField(max_length=200, choices=requirements_items)
    payment = models.CharField(max_length=200)

