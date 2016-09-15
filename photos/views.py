from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from photos.models import Photo, VISIBILITY_PUBLIC
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
    # photos = Photo.objects.all().order_by('-created_at') me trae todas las fotos de la base de datos. como un select *

    photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')
    context = {'photo_list': photos[:4]}
    return render(request, 'photos/home.html', context)


def photo_detail(request, pk):
    """
    Renderiza el detalle d ela imagen
    :param request:
    :return:
    """

    possible_photos = Photo.objects.filter(pk=pk)
    if len(possible_photos) == 0:
            return HttpResponseNotFound("La imagen que buscas no existe")
    elif len(possible_photos) > 1:
            return HttpResponse("Multiples opciones", status=300)

    photo = possible_photos[0] if len(possible_photos) > 0 else None
    context = {'photo': photo}

    return render(request, 'photos/photo_detail.html', context)
