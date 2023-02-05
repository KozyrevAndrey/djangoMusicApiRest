from rest_framework import generics

from musicApi.models import Performer, Album, Song
from musicApi.serializers import PerformerSerializer, AlbumSerializer, SongSerializer


class PerformerList(generics.ListCreateAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
