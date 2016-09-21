from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from photos.forms import PhotoForm
from photos.models import Photo, VISIBILITY_PUBLIC
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de fotos

        :param request: objeto HttpRequest con los datos de la peticion
        :return: objecto HttpResponse con los datos de la respuesta
        """

        quixote = """ En un lugar con multilinea se puede
        agregar que hermoso"""

        # order_bay para obtener los resultados de la query en orden del campo creado, y el guion es desendente.
        # photos = Photo.objects.all().order_by('-created_at') me trae todas las fotos de la base de datos. como un select *

        photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at').select_related("owner")
        context = {'photo_list': photos[:4]}
        return render(request, 'photos/home.html', context)

class PhotoDetailView(View):
    def get(self, request, pk):
        """
        Renderiza el detalle d ela imagen
        :param request:
        :return:
        """

        possible_photos = Photo.objects.filter(pk=pk).select_related("owner") #inner join para evitar hacer muchas peticiones
        if len(possible_photos) == 0:
                return HttpResponseNotFound("La imagen que buscas no existe")
        elif len(possible_photos) > 1:
                return HttpResponse("Multiples opciones", status=300)

        photo = possible_photos[0] if len(possible_photos) > 0 else None
        context = {'photo': photo}

        return render(request, 'photos/photo_detail.html', context)


class PhotoCreationView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear una foto
        :param request:
        :return:
        """

        message = ""
        photo_form = PhotoForm()
        context = {'form': photo_form, 'message': message}
        return render(request, 'photos/photo_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear una foto y en caso de que la peticion sea post, la valida y la crea en caso de que
        sea valida.
        :param request:
        :return:
        """

        message = ""
        photo_with_user = Photo(owner=request.user)
        photo_form = PhotoForm(request.POST, instance = photo_with_user)

        if photo_form.is_valid():
            new_photo = photo_form.save()
            photo_form = PhotoForm()  # limpia los campos para que se pueda crear una nueva foto.
            message = "Foto creada satisfactoriamente <a href='{0}'> Ver foto </a>".format(
                reverse('photos_detail', args=[new_photo.pk])
            )

        context = {'form': photo_form, 'message': message}
        return render(request, 'photos/photo_creation.html', context)



# multiherencia con el validador de login, se puede usar tambien el decorador pero en este caso usamos la clase
# LoginRequiredMixin


class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photos/photo_list.html'

    # tambien se puede usar la siguiente funcion para validar al usuario logueado
    """
    @method_decorator(login_required())
    def get(self, request):
        return super().get(request)
    """

    # en vez de utilizar el query set de objecto.all que es el de defecto, consultar por usuario.
    def get_queryset(self):
        result = super().get_queryset().filter(owner=self.request.user)

        return result



