from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from music.models import Song, Album, Artist


class ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'






class AlbumSerializers(serializers.ModelSerializer):
    artist = ArtistSerializers()
    class Meta:
        model = Album
        fields = '__all__'





class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializers()
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'cover', 'source')


    def validate_source(self, value):
        if not value.endswith('.mp3'):
            raise ValidationError(detail='Mp3 file is required')
        return value