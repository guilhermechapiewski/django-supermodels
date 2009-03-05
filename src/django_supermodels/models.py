from django.db.models.base import ModelBase as DjangoModelBase
from django.db.models import Model as DjangoModel

class DynamicFinders(DjangoModelBase):
    def __getattribute__(cls, name):
        if name.startswith("find_by_"):
            def find_by(*args, **kwargs):
                print "Missing method %s called (args = %s) and (kwargs = %s)" % (name, str(args), str(kwargs))
            return find_by

class SuperModel(DjangoModel):
    __metaclass__ = DynamicFinders

    class Meta:
            abstract = True