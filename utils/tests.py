from django.test import TestCase
from django.test.client import RequestFactory
from django.conf import settings

from utils import context_processors


class ContextProcessorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    
    def test(self):
        request = self.factory.get('/')
        saved_settings = context_processors.get_settings(request)['MY_SETTINGS']
        self.assertEqual(settings, saved_settings)
        
        
