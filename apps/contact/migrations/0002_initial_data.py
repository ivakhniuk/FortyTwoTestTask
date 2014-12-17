# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.auth.models import User

from contact.models import Person


class Migration(DataMigration):

    def forwards(self, orm):
        bio = Person(first_name="Volodymyr", last_name="Ivakhniuk",
                    birth_date="1990-04-04", email="ivakhniuk@gmail.com",
                    jabber="ivakhniuk@jabbim.com", skype="vovasan9",
                    other_contacts="tel: +380978362235", bio="Was born...")
        user = User(pk=1, username="admin", is_active=True,
                    is_superuser=True, is_staff=True,
                    last_login="2011-09-01T13:20:30+03:00", password="admin",
                    email="ivakhniuk@gmail.com",
                    date_joined="2011-09-01T13:20:30+03:00")
        bio.save()
        user.save()


    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")


    models = {
        u'contact.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contact']
