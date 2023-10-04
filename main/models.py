from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    myname = models.CharField(max_length=255, default='')
    myclass = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    amount = models.IntegerField()
    date_added = models.DateField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, default='')