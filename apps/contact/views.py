from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from contact.models import Person


def person_view(request):
    person = get_object_or_404(Person, pk=1)
    return render(request, "contact/person.html", {'person': person})
