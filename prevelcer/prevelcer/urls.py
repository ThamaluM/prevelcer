"""prevelcer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views
import rest_framework.authtoken.views as rest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user/',include('users.urls')),
    path('accounts/',include("django.contrib.auth.urls")),
    path('',views.home),
    path('api-token-auth/', rest_views.obtain_auth_token, name='api-token-auth'),
    path('pressure/',include('pressure_data.urls')),
    path('notify',views.send_notification)
]
