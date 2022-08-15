from pyexpat import model
from django.db import models

# Create your models here.

class APi_default(models.Model):
    Firstname = models.CharField(max_length=100,blank=True,null=True,default="null")
    Lastname = models.CharField(max_length=100,blank=True,null=True,default="null")
    Email = models.EmailField(max_length=100,blank=True,null=True,default="null")
    unique = models.CharField(max_length=100,blank=True,null=True,default="null")

    def __str__(self):
         return self.Firstname


