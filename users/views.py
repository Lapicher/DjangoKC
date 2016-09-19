from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    :param request:
    :return:
    """

    error_messages = ""
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('pwd')

        user = authenticate(username=username, password=password)
        if user is None:
            error_messages = "Usuario o contraseña incorrecto"
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                error_messages = "Cuenta de usuario inactiva"


    return render(request, 'users/login.html', {'error':error_messages})


def logout(request):
    """
    Hace el logout de un usuario redirige al login
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('/')

