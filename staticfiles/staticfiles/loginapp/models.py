from django.db import models
from requests import request

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    sex=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)

