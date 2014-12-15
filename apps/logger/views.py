from django.shortcuts import render
from django.contrib.auth import authenticate

from logger.models import RequestStore
from logger.forms import LoginForm


def logger_view(request):
    requests = RequestStore.objects.order_by('-date_time')[:10]
    return render(request, 'logger/requests_list.html', {'requests': requests})
    
