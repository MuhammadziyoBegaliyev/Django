from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from music.models import Song
from music.serializers import SongSerializer


# Create your views here.


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer