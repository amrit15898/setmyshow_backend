from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
artist_type = (("a", "a"), ("b", "b"), ("c", "c"))
class User(AbstractUser):
    artist_type_band = models.CharField(max_length=200, choices=artist_type,  null=True , blank=True )
    contact = models.CharField(max_length=20, null=True, blank=True)


  