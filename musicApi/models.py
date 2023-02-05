from django.db import models


class Performer(models.Model):
    performer_name = models.CharField(max_length=200, verbose_name='Исполнитель')

    def __str__(self):
        return self.performer_name


class Song(models.Model):
    song_name = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.song_name


class Album(models.Model):
    fk_album_performer = models.ForeignKey(Performer, on_delete=models.CASCADE, verbose_name='Исполнитель Альбома')
    release_year = models.DateField(verbose_name='Год Выпуска')
    song_number_album = models.IntegerField(null=True, blank=True)
    fk_song_name = models.ForeignKey(Song, related_name='album_numbers', on_delete=models.DO_NOTHING,
                                     verbose_name='Внешний ключ песни')

    def __str__(self):
        return str(self.fk_song_name)
