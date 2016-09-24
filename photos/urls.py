from django.conf.urls import url

from photos.api import PhotoListAPI, PhotoDetailAPI
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView


urlpatterns = [
     # el mas es que el los numeros se pueden repetir una o mas veces.
    # entre parentesis se pone la variable a capturar, y entre menor y mayor que va el nombre del parametro.

    url(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_my_photos'),
    url(r'^$', HomeView.as_view(), name='photos_home'),


    # URLS APis
    url(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='api_photos_list'),
    url(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view(), name='api_photos_detail')
]
