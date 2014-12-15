from django.test import TestCase
from django.test import Client
from django.utils import timezone

from logger.models import RequestStore

'''
class LoggerTest(TestCase):
    
    def test_logger(self):
        client = Client()
        response1 = client.get('/logger')
        date_time = timezone.now()
        request = RequestStore.objects.order_by('date_time')[0]
        response2 = client.get('/logger')
        
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(date_time.hour, request.date_time.hour)
        self.assertEqual(date_time.minute, request.date_time.minute)
        self.assertContains(response2, str(date_time.year))
        '''
