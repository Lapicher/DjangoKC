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

    # metodo que nos sirve para crear la foto con el propietario que se logueo en la API.
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualizacion y borrado de fotos
    """
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PhotoQueryset.get_photos_by_user(self.request.user)

    # metodo para que al modificar solo se modifique la foto propietaria del usuario autentificado.
    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
