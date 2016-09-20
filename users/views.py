from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


# Create your views here.
from users.forms import LoginForm


def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    :param request:
    :return:
    """

    error_messages = ""
    login_form = LoginForm(request.POST) if request.method == "POST" else LoginForm() # para que mantenga los datos en los campos.
    if request.method == "POST":
        if login_form.is_valid(): # funcion donde django valida la entrada de los datos, aun no es sqlinjectiongit etc.

            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')

            user = authenticate(username=username, password=password)
            if user is None:
                error_messages = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
                else:
                    error_messages = "Cuenta de usuario inactiva"

    context = {'error': error_messages, 'form': login_form}
    return render(request, 'users/login.html', context)


def logout(request):
    """
    Hace el logout de un usuario redirige al login
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('/')


