from django.db import models
from django.contrib.localflavor.us.models import USStateField

from const import STATUS_CHOICES 


class Person(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    dob = models.DateField('Date of Birthday')
    city = models.CharField('City', max_length=100)
    state = USStateField('State')
    email = models.EmailField('Email')
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Relationship(models.Model):
    person1 = models.ForeignKey(Person, verbose_name='Person1',
                                    related_name='person1')
    person2 = models.ForeignKey(Person, verbose_name='Person2',
                                    related_name='person2')
    status = models.SmallIntegerField('Status', choices=STATUS_CHOICES,
                                      null=True, blank=True)
