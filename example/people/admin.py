from example.people.models import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)