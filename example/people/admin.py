from example.people import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)