from django.contrib import admin
from .models import Performer, Song, Album


admin.site.register(Performer)
admin.site.register(Album)
admin.site.register(Song)
