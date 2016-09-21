"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView
from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view()),  # el mas es que el los numeros se pueden repetir una o mas veces.
    # entre parentesis se pone la variable a capturar, y entre menor y mayor que va el nombre del parametro.
    url(r'^create$', PhotoCreationView.as_view()),
    url(r'^photos/$', PhotoListView.as_view()),
    url(r'^$', HomeView.as_view())
]
