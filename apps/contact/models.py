from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.CharField(max_length=50)
    jabber = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    other_contacts = models.TextField(max_length=1000)
    bio = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.first_name + " " + self.last_name
