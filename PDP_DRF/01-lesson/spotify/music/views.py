from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from music.models import Song, Album, Artist
from music.serializers import SongSerializer, AlbumSerializers, ArtistSerializers


# Create your views here.


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers