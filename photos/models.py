from django.db import models
from django.contrib.auth.models import User

# Create your models here.


LICENCSE_COPYRIGHT = "RIG"
LICENSE_COPYLEFT = "LEF"
LICENSE_CC = "CC"

LICENSES = (
    (LICENCSE_COPYRIGHT, 'Copyright'),
    (LICENSE_COPYLEFT, 'Copyleft'),
    (LICENSE_CC, 'Creative Commons')
)

VISIBILITY_PUBLIC = "PUB"
VISIBILITY_PRIVATE = "PRI"

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Publica'),
    (VISIBILITY_PRIVATE, 'Privada')
)


class Photo(models.Model):


    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    # file = models.FileField(upload_to="uploads"), # para subir fotos al servidor, si hay repetidos django se encarga, hermoso.
    description = models.TextField(null=True, blank=True) # null= true, indica que el campo es opcional, blank puede ser vacio.
    license = models.CharField(max_length=3, choices=LICENSES, default=LICENSE_CC)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):  # mifoto.__str__() para que en el admin no se vea como objeto Photo y mejor el nombre de la foto
        return self.name

