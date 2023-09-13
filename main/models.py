from django.db import models

# Create your models here.
class Item(models.Model):
    myname = models.CharField(max_length=255, default='')
    myclass = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()