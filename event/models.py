import json

from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Event(models.Model):
    title = models.CharField(max_length=80)
    user_id = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=30)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    time_str = models.CharField(max_length=10, blank=True)
    # photo = models.ImageField(blank=True)

    repeat_mode = models.CharField(max_length=20)  # once_week once_2week once

    tags = TaggableManager()

    created_date = models.DateTimeField(default=timezone.now)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    # def __str__(self):
    #     return s
