from datetime import date

from django.test.client import Client
from django.test import TestCase

from models import *


class PersonTest(TestCase):
    
    def setUp(self):
        self.person1 = Person.objects.create(first_name='John', last_name='Smith',
                                             dob='1975-08-15', city='Los Angeles',
                                             state='CA', email='test@test.com')
        self.person2 = Person.objects.create(first_name='Anna', last_name='Smith',
                                             dob='1953-08-15', city='Los Angeles',
                                             state='CA', email='test3@test.com')
        self.person3 = Person.objects.create(first_name='Tom', last_name='Smith',
                                             dob='1948-08-15', city='Los Angeles',
                                             state='CA', email='test2@test.com')
        self.rs1 = Relationship.objects.create(person1=self.person1,
                                               person2=self.person2,
                                               status=3)
        self.rs2 = Relationship.objects.create(person1=self.person1,
                                               person2=self.person3,
                                               status=4)
        self.rs3 = Relationship.objects.create(person1=self.person3,
                                               person2=self.person2,
                                               status=8)

        self.c = Client()
    
    def test_get_index(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Smith', status_code=200)
   
    def test_person_creation(self):
        response = self.c.post('/add/', {'first_name': u'Greg', 'last_name': u'Johns', 
                                        'email': u'gfborn@gmail.com', 'city': 'Chicago',
                                        'state': 'AL', 'dob': '1934-05-07',
                                        'person': self.person3.id, 'status': 2})
        self.assertEqual(response.status_code, 302)
        
    def test_relationship(self):
        response = self.c.get('/')
        self.assertContains(response, 'Anna Smith Mam', status_code=200)
        self.assertContains(response, 'Tom Smith Dad', status_code=200)
