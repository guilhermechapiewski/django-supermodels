from django.db import models
from django_supermodels.db import supermodels

class Person(supermodels.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField()
    country = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name