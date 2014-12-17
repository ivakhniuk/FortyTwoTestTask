from logger.models import RequestStore
from django.utils import timezone


class SaveRequest(object):
    def process_request(self, request):
        new_request = RequestStore()
        new_request.path = request.get_full_path()
        new_request.method = request.method
        new_request.date_time = timezone.now()
        if request.user.is_authenticated():
            new_request.user = request.user

        new_request.save()
