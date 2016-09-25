from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotoQueryset


class PhotoListAPI(ListCreateAPIView):
    """
    End point de listado y creacion de fotos
    """
    # queryset = Photo.objects.all()
    # serializer_class = PhotoListSerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return PhotoQueryset.get_photos_by_user(self.request.user)

    # se comenta la linea anterior para permitir al metodo siguiente seleccionar que serializador escoger.
    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualizacion y borrado de fotos
    """
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PhotoQueryset.get_photos_by_user(self.request.user)
