from rest_framework import serializers, viewsets
from .models import Task
from django.contrib.auth import get_user_model


# Serializers define the API representation.
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'user', 'priority',
                  'created_at', 'updated_at']


# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
