"""
# django-supermodels - extension for Django models

This is a toy to implement dynamic finders on Django models, similar to 
what you can find in Rails.

Examples:

>>> Person.objects.find_by_id(1)
>>> Person.objects.find_by_name('Guilherme Chapiewski')
>>> Person.objects.find_by_id_and_name(1, 'Guilherme Chapiewski')

Developed by:
-- Guilherme Chapiewski - http://gc.blog.br
 
Contributors:
-- Oliver Andrich - http://oliverandrich.net/
"""

from django.db.models.base import ModelBase as DjangoModelBase
from django.db.models import Model as DjangoModel
from django.db.models import Manager as DjangoManager

class DynamicFinders(DjangoModelBase):
    def __getattribute__(obj, *args, **kwargs):
        print 'metaclass getattribute invoked'
        print 'missing method %s called (args = %s) and (kwargs = %s)' % (args[0], str(args), str(kwargs))
        
        method_name_called = args[0]
        if method_name_called.startswith('find_by_'):
            print '-- recognized call to find_by_'
            print "-- found it!" if "WILD_find_by" in type(obj).__dict__ else "-- not found"
            #TODO: return super(DynamicFinders, self).__getattribute__('WILD_find_by', *args, **kwargs)
            
        #TODO: return super(DynamicFinders, self).__getattribute__(obj, *args, **kwargs)

    @classmethod
    def WILD_find_by(cls, *args, **kwargs):
        print '---- resolved'

class FindByManager(DjangoManager):
    def __getattribute__(self, name):
        if name and name.startswith('find_by_'):
            print '-- recognized call to find_by_'
            fields = name.replace('find_by_', '').split('_and_')
            print '-- fields = %s' % fields
            def find_by(*args):
                filter_dict = dict(zip(fields, args))
                print '-- filter_dict = %s' % filter_dict
                return self.filter(**filter_dict)
            return find_by
        return super(FindByManager, self).__getattribute__(name)

class Model(DjangoModel):
    #TODO: __metaclass__ = DynamicFinders 
    objects = FindByManager()
        
    class Meta(object):
            abstract = True
