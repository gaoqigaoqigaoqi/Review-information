from django.db import models

# Create your models here.
class Suser(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    nikname = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
