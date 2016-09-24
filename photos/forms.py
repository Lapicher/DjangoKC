from django.core.exceptions import ValidationError

from photos.models import Photo
from django.forms import ModelForm

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        # fields = ['visibility', 'license'] seleccionamos el orden de los campos a mostrar.
        exclude = ['owner']

