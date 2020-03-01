import json
import re
import datetime as dt

from .models import Event
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core import serializers

time_re = re.compile(r'^(?P<hours>\d\d):(?P<min>\d\d) (?P<day>\d+)-(?P<month>\d+)-(?P<year>\d{4})$')

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
    print(req.body)
    data = json.loads(req.body.decode('utf8'))
    event = Event.objects.create(
        # title=data['title'],
                  location=data['location'],
                  description=data['description'],
                  start_time=dt.datetime.strptime(data['start_time'], '%H:%M %d.%m.%Y'),
                  # end_time=dt.datetime.strptime(data['end_time'], '%H:%M %d-%m-%Y'),
                  tags=data['tags'],
                  img_url=data['img_url'])
                  # user_id=int(data.['user_id']))
    res = event.save()
    return HttpResponse(event.id)

