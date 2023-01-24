from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model


class Task(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(default='', blank=True, max_length=800)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
