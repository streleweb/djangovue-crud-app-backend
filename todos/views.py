from rest_framework import serializers, viewsets, permissions, authentication
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin


# Serializers define the API representation.
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'completed', 'priority',
                  'created_at', 'updated_at']


# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet, PermissionRequiredMixin):
    authentication_classes = [authentication.TokenAuthentication]
    # user must be authenticated to use this API
    permission_classes = [permissions.IsAuthenticated]
    permission_required = 'todos.change_task'
    serializer_class = TaskSerializer

    # queryset = Task.objects.filter(user_id = request.user.id)

    def get_queryset(self):
        user_id = self.request.user.id  # get the ID of the currently logged-in user
        queryset = Task.objects.filter(
            user_id=user_id)  # filter tasks by user ID
        return queryset
