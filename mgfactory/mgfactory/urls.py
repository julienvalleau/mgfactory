"""mgfactory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^rawmaterial/', include('rawmaterial.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', RedirectView.as_view(url='dashboard/', permanent=True)),
]