from django.conf import settings


def get_settings(request):
    return {'MY_SETTINGS': settings}
