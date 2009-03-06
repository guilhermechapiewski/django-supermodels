"""
# django-supermodels - extension for Django models

This is a toy to implement dynamic finders on Django models, similar to 
what you can find in Rails.

Examples:

    >>> Person.objects.all()
    [Person[name=Guilherme Chapiewski, age=123, birth_date=2009-03-06, country=Brazil], Person[name=Hoover Orsi, age=34, birth_date=2009-03-08, country=Brazil]]

    >>> Person.objects.find_by_name('Guilherme Chapiewski')
    [Person[name=Guilherme Chapiewski, age=123, birth_date=2009-03-06, country=Brazil]]

    >>> Person.objects.find_by_id(2)
    [Person[name=Hoover Orsi, age=34, birth_date=2009-03-08, country=Brazil]]

    >>> Person.objects.find_by_name_and_id('Guilherme Chapiewski', 89732)
    []

    >>> Person.objects.find_by_id_and_name(1, 'Guilherme Chapiewski')
    [Person[name=Guilherme Chapiewski, age=123, birth_date=2009-03-06, country=Brazil]]

    >>> Person.objects.find_by_nonexistingfield('something')
    Cannot resolve keyword 'nonexistingfield' into field. Choices are: age, birth_date, country, id, name

Developed by:
-- Guilherme Chapiewski - http://gc.blog.br
 
Thanks to these guys for their ideas and contributions:
-- Luciano Ramalho - http://ramalho.org
-- Oliver Andrich - http://oliverandrich.net
"""

from django.db.models.base import ModelBase as DjangoModelBase
from django.db.models import Model as DjangoModel
from django.db.models import Manager as DjangoManager

# http://docs.python.org/reference/datamodel.html#new-style-special-lookup
class DynamicFinders(DjangoModelBase):
    def __getattribute__(obj, *args, **kwargs):
        print 'metaclass getattribute invoked'
        print 'missing method %s called (args = %s) and (kwargs = %s)' % (args[0], str(args), str(kwargs))
        
        method_name_called = args[0]
        if method_name_called.startswith('find_by_'):
            print '-- recognized call to find_by_'
            print "-- found it!" if "WILD_find_by" in type(obj).__dict__ else "-- not found"
            #TODO: this call does not work
            # return super(DynamicFinders, self).__getattribute__('WILD_find_by', *args, **kwargs)
            
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
    #TODO: the original idea (without the .objects thing)
    # __metaclass__ = DynamicFinders 
    objects = FindByManager()
        
    class Meta(object):
            abstract = True
