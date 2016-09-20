from django.core.exceptions import ValidationError

from photos.models import Photo
from django.forms import ModelForm

BADWORDS = (
            "Caranabo",
            "Carapan",
            "Chimpamonas",
            "Chupaescrotos",
            "Cuerpoescombro"
            )

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        # fields = ['visibility', 'license'] seleccionamos el orden de los campos a mostrar.
        exclude = ['owner']

    def clean(self):
        """
        Valida que la descripcion no contenga ninguna palabrota
        :return: diccionario con los datos limpios y validados
        """
        cleaned_data = super().clean() # obtenelos los datos del formulario limpios que hace django por nosotros.
        descripcion = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in descripcion:
                raise ValidationError("La palabra {0} no esta permitida".format(badword))
        return cleaned_data

