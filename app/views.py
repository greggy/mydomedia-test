from django.http import HttpResponseRedirect

from models import Person, Relationship
from forms import PersonForm
from lib import render_to


@render_to('index.html')
def index(request):
    """
    
    """
    families = Person.objects.values_list('last_name', flat=True).distinct()
    persons = Person.objects.all()
    return {'persons': persons}


@render_to('add.html')
def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_person = form.save()
            if cd.get('person'):
                rs = Relationship.objects.create(person1=cd.get('person'),
                                                 person2=new_person,
                                                 status=cd.get('status'))
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()
    return {'form': form}
