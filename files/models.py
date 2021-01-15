from django.db import models

# Create your models here.
class MainModel(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=200,blank=True,null=True)

def __str__(self):
    return self.name

      