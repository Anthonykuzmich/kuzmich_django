from django.shortcuts import render, redirect
from .models import MusicBand, Album, Track


def home(request):
    return render(request, 'choose.html')


def read_albums(request):
    acdc_albums = MusicBand.objects.get(id=1).albums.all()
    imagine_dragons_albums = MusicBand.objects.get(id=2).albums.all()
    context = {'acdc_albums': acdc_albums,
               'dragons_albums': imagine_dragons_albums}
    return render(request, 'read.html', context)

def albums_groups(request):
    band_nineties = MusicBand.objects.filter(foundation_year='1990').first()
    albums = band_nineties.albums.all()
    context = {'band_nineties': band_nineties,
               'albums': albums}
    return render(request, 'band_nineties.html', context)


def read_albums_tracks(request):
    first_acdc_album_tracks = Album.objects.get(id=1).tracks.all()
    second_acdc_album_tracks = Album.objects.get(id=4).tracks.all()
    first_album_tracks = Album.objects.get(id=2).tracks.all()
    second_album_tracks = Album.objects.get(id=3).tracks.all()
    context = {'first_dragon_album_tracks': first_album_tracks,
               'second_dragon_album_tracks': second_album_tracks,
               'first_acdc_album_tracks': first_acdc_album_tracks,
               'second_acdc_album_tracks': second_acdc_album_tracks}

    return render(request, 'read_albums_tracks.html', context)


# def read_models(request):
#     acdc_albums = MusicBand.objects.get(id=1).albums.all()
#     first_acdc_album_tracks = Album.objects.get(id=1).tracks.all()
#     second_acdc_album_tracks = Album.objects.get(id=4).tracks.all()
#     acdc_tracks = MusicBand.objects.get(id=1).tracks.all()
#
#     imagine_dragons_albums = MusicBand.objects.get(id=2).albums.all()
#     first_album_tracks = Album.objects.get(id=2).tracks.all()
#     second_album_tracks = Album.objects.get(id=3).tracks.all()
#     track_imagine_dragons = MusicBand.objects.get(id=2).tracks.all()
#     context = {'dragons_albums': imagine_dragons_albums,
#                'first_dragon_album_tracks': first_album_tracks,
#                'second_dragon_album_tracks': second_album_tracks,
#                'tracks_imagine_dragons': track_imagine_dragons,
#                'acdc_albums': acdc_albums,
#                'first_acdc_album_tracks': first_acdc_album_tracks,
#                'second_acdc_album_tracks': second_acdc_album_tracks,
#                'acdc_tracks': acdc_tracks}
#     return render(request, 'read.html', context)
