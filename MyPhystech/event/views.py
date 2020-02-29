from .models import Event
from taggit.models import Tag
from django.http import HttpResponse


def home_view(request):
    request.userID = 11
    return HttpResponse(request)


def add_event(request):
    event = Event(title='This is title', location='It will be here')
    event.save()
    return HttpResponse(request)
