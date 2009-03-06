from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'people.views.find_by'),
)