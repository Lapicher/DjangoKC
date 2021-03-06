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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from files.views import FileViewSet
from photos import urls as photos_urls
from users import urls as users_urls
"""
import photos.urls
import users.urls
"""

router = DefaultRouter()
router.register('api/1.0/files', FileViewSet )

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include(photos_urls)),
    url(r'', include(users_urls)),

    url(r'', include(router.urls))
]
