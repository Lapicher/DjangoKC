from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from photos.models import Photo
from django.shortcuts import render


def home(request):
    """
    Renderiza el home con un listado de fotos

    :param request: objeto HttpRequest con los datos de la peticion
    :return: objecto HttpResponse con los datos de la respuesta
    """

    quixote = """ En un lugar con multilinea se puede
    agregar que hermoso"""

    # order_bay para obtener los resultados de la query en orden del campo creado, y el guion es desendente.
    photos = Photo.objects.all().order_by('-created_at')  # me trae todas las fotos de la base de datos. como un select *
    context = {'photo_list': photos[:4]}
    return render(request, 'photos/home.html', context)

