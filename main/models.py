from django.db import models

# Create your models here.
class Product(models.Model):
    myname = models.CharField(max_length=255, default='')
    myclass = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    amount = models.IntegerField()
    date_added = models.DateField(auto_now=True, null=True)