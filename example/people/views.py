from example.people.models import Person
from django.http import HttpResponse

def find_by(request):
    p = Person.objects.find_by_name('Guilherme Chapiewski')
    html = '<html><body><h2>%s</h2><h2>%s</h2></body></html>' % ('>>> Person.objects.find_by_name(\'Guilherme Chapiewski\')', str(p))
    return HttpResponse(html)