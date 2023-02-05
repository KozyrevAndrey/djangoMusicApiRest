from django.urls import path
from musicApi.apiViews import (
    PerformerList,
    AlbumList,
    SongList)

urlpatterns = [
    path('api/perfomer', PerformerList.as_view()),
    path('api/album', AlbumList.as_view()),
    path('api/song', SongList.as_view()),
]
