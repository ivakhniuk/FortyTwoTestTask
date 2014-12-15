from django.db import models

from django.contrib.auth.models import User


class RequestStore(models.Model):
    date_time = models.DateTimeField()
    path = models.CharField(max_length=255)
    host = models.CharField(max_length=100)
    method = models.CharField(max_length=4)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.path
