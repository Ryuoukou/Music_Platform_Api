from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSet, AlbumViewSet, TrackViewSet, PlaylistViewSet


router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns =[
    path('api/', include(router.urls)),
]
