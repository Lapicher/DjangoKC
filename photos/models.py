from django.db import models

# Create your models here.


class Photo(models.Model):

    LICENSES = (
        ('RIG', 'Copyright'),
        ('LEF', 'Copyleft'),
        ('CC', 'Creative Commons')
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    license = models.CharField(max_length=3, choices=LICENSES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # mifoto.__str__() para que en el admin no se vea como objeto Photo y mejor el nombre de la foto
        return self.name

