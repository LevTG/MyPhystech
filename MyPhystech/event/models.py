from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.CharField()
    event_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    photo = models.ImageField(blank=True)

    repeat_mode = models.CharField()  # once_week once_2week once

    tags = TaggableManager()

    created_date = models.DateTimeField(default=timezone.now)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title