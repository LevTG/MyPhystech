import json

from .models import Event
from taggit.models import Tag
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core import serializers

@api_view(['GET'])
def home(request):
    return HttpResponse('Hello world')


@api_view(['GET'])
def all_ev(request):
    es = Event.objects.all()
    data = serializers.serialize('json', es)
    return HttpResponse(data)


@api_view(['POST', 'PUT'])
def add_event(req):
    # print(req.POST)
    # print(req.body)
    data = json.loads(req.body.decode('utf8'))
    event = Event.objects.create(title=data['title'],
                  location=data['location'],
                  description=data['description'])
                  # event_date=data.date)
                  # user_id=int(data.['user_id']))
    event.save()
    return HttpResponse(event.id)

#
# def get_events(req):
#     data = json.loads(req.body.decode('utf8'))
#     es = Event.objects.filter(id=data.userID,
#                               start_time=data.date,
#                               tags=)
#     data = serializers.serialize('json', es)
#     return HttpResponse(data)
