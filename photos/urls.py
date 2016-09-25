from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView

router = DefaultRouter()
router.register('api/1.0/photos', PhotoViewSet, 'api_photos_')

urlpatterns = [
     # el mas es que el los numeros se pueden repetir una o mas veces.
    # entre parentesis se pone la variable a capturar, y entre menor y mayor que va el nombre del parametro.

    url(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_my_photos'),
    url(r'^$', HomeView.as_view(), name='photos_home'),


    # URLS APis
    url(r'', include(router.urls)),
]
