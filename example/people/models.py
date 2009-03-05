'''
import os, sys
aqui = os.path.abspath(os.path.split(__file__)[0])
acima = os.path.split(aqui)[0]
sys.path.append(acima)
from django.core.management import setup_environ
import settings
setup_environ(settings)
'''

from django.db import models
from django_supermodels.models import SuperModel

class Person(SuperModel):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField()
    country = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

'''    
if __name__ == "__main__":
    print Person.find_by_id(1)
    print Person.find_by_name("gc")
'''