from rest_framework import serializers
from .models import Performer, Album, Song


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ['id', 'performer_name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['fk_album_performer', 'release_year']


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('song_number_album',)


class SongSerializer(serializers.ModelSerializer):
    album_numbers = NumberSerializer(many=True)

    class Meta:
        model = Song
        fields = ['id', 'song_name', 'album_numbers']


