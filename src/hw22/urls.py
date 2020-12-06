from django.urls import path
from .views import home, read_albums, read_albums_tracks, albums_groups

urlpatterns = [
    path('home', home, name='home'),
    path('read_albums', read_albums, name='read_albums'),
    path('read_albums_tracks', read_albums_tracks, name='read_albums_tracks'),
    path('album_groups', albums_groups, name = 'album_groups')
]
