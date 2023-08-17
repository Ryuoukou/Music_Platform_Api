from django.contrib import admin
from .models import Artist, Album, Track, Playlist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'album')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', )
