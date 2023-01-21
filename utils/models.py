from django.db import models


class Timestamps(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # correct way to structure mixins, otherwise it might trigger consistent method resolution order exception in todos
    class Meta:
        abstract = True
