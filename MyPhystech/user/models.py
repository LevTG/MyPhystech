from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    fist_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    course = models.IntegerField()
    department = models.CharField(max_length=40)
    degree = models.IntegerField()

    dometory = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.first_name