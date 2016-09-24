from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoListAPI(ListCreateAPIView):
    """
    End point de listado y creacion de fotos
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualizacion y borrado de fotos
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
