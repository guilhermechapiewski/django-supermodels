from example.people.models import Person
from django.http import HttpResponse

def find_by(request):
    html = '<html><body>'
    
    everyone = Person.objects.all()
    html += '<p>%s</p><p>%s</p><br>' % ('>>> Person.objects.all()', str(everyone))
    
    p = Person.objects.find_by_name('Guilherme Chapiewski')
    html += '<p>%s</p><p>%s</p><br>' % ('>>> Person.objects.find_by_name(\'Guilherme Chapiewski\')', str(p))
    
    p = Person.objects.find_by_id(2)
    html += '<p>%s</p><p>%s</p><br>' % ('>>> Person.objects.find_by_id(2)', str(p))
    
    p = Person.objects.find_by_name_and_id('Guilherme Chapiewski', 89732)
    html += '<p>%s</p><p>%s</p><br>' % ('>>> Person.objects.find_by_name_and_id(\'Guilherme Chapiewski\', 89732)', str(p))
    
    p = Person.objects.find_by_id_and_name(1, 'Guilherme Chapiewski')
    html += '<p>%s</p><p>%s</p><br>' % ('>>> Person.objects.find_by_id_and_name(1, \'Guilherme Chapiewski\')', str(p))
    
    try:
        p = Person.objects.find_by_nonexistingfield('something')
    except Exception, e:
        html += '<p>%s</p><p>%s</p><br>' % ('>>> Person.objects.find_by_nonexistingfield(\'something\')', str(e))
        
    
    html += '</body></html>'
    return HttpResponse(html)