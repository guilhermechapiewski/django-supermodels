from django.db.models.base import ModelBase as DjangoModelBase
from django.db.models import Model as DjangoModel

class DynamicFinders(DjangoModelBase):
    def __getattribute__(*args, **kwargs):
        print 'Metaclass getattribute invoked'
        print 'Missing method %s called (args = %s) and (kwargs = %s)' % (args[1], str(args), str(kwargs))
        
        method_name_called = args[1]
        if method_name_called.startswith('find_by_'):
            print '-- recognized find_by_'
            print "-- achei!" if "_find_by" in type.__dict__ else "-- nao achei"
            return super(DynamicFinders, self).__getattribute__('_find_by')
            
        return type.__getattribute__(*args, **kwargs)
    
class Model(DjangoModel):
    __metaclass__ = DynamicFinders

    @classmethod
    def _find_by(cls, *args, **kwargs):
        print '---- resolved'
        
    class Meta(object):
            abstract = True