from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model


class Note(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class NoteItem(Timestamps, models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
