from django.db import models
from django_supermodels.db import supermodels

class Person(supermodels.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField()
    country = models.CharField(max_length=200)
    
    def __repr__(self):
        return 'Person[name=%s, age=%d, birth_date=%s, country=%s]' % (self.name, self.age, self.birth_date, self.country)
    
    class Meta(object):
        verbose_name_plural = 'people'