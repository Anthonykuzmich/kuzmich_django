from django.db import models


class MusicBand(models.Model):
    band_name = models.CharField(max_length=20)
    foundation_year = models.CharField(max_length=10)
    music_style = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.band_name}'


class Track(models.Model):
    duration = models.CharField(max_length=10)
    track_name = models.CharField(max_length=20)
    band = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='tracks')
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL, related_name='tracks')

    def __str__(self):
        return f'{self.track_name}'


class Album(models.Model):
    album_name = models.CharField(max_length=20)
    release_year = models.CharField(max_length=10)
    band = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='albums')
    def __str__(self):
        return f'{self.album_name}'
