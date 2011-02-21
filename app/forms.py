from django import forms

from models import Person
from const import STATUS_CHOICES


class PersonForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    empty_label=" -- ", 
                                    label='Related Person', 
                                    required=False) 
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'dob', 'city',
                  'state', 'email', 'person', 'status')
        
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = [(0, ' -- ')] + list(STATUS_CHOICES)