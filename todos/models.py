from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model


class Task(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(default='', blank=True, max_length=800)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        default='lightblue', blank=True, null=True, max_length=9)

    def __getattribute__(self, name):
        attr = models.Model.__getattribute__(self, name)
        if name == 'priority' and not attr:
            return 'lightblue'
        return attr

    def __str__(self):
        return self.title
