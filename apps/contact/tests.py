from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from contact.models import Person


class ResumeTest(TestCase):

    def test_index(self):
        client = Client()
        response = client.get('/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context[-1]['person']), 'Volodymyr Ivakhniuk')
        self.assertContains(response, "Volodymyr")
        
        
