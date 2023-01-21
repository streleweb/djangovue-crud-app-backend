

from rest_framework import serializers, viewsets
from .models import Note, NoteItem
from django.contrib.auth import get_user_model


# Serializers define the API representation.
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    class Meta:
        model = Note
        fields = ['name', 'description', 'user',
                  'created_at', 'updated_at']


class NoteItemSerializer(serializers.HyperlinkedModelSerializer):
    note = serializers.PrimaryKeyRelatedField(
        queryset=Note.objects.all())

    class Meta:
        model = NoteItem
        fields = ['text', 'note',
                  'created_at', 'updated_at']


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteItemViewSet(viewsets.ModelViewSet):
    queryset = NoteItem.objects.all()
    serializer_class = NoteItemSerializer
