from django.test import TestCase, Client
from django.utils import timezone
from django.test.client import RequestFactory
from django.contrib.auth.models import User

from logger.models import RequestStore
from logger.middleware import SaveRequest


class LoggerTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/logger/')
        self.request.user = User.objects.get(username="admin")
        self.client = Client()
        self.save_request_instance = SaveRequest()
    
    def test_logger(self):
        self.save_request_instance.process_request(self.request)
        response = self.client.get('/logger/')
        date_time = timezone.now()
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(date_time.minute))
        self.assertContains(response, '/logger/')
        self.assertContains(response, "admin")
        
