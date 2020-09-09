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
from .views import UserRecordView,ProfileRecordView

app_name = 'api'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('get/',views.test_get,name = 'test_get'),
    path('user/', UserRecordView.as_view(), name='users'),
    path('register/',views.create_account,name="create_account"),
    path('profile/', ProfileRecordView.as_view(), name='users'),
]






