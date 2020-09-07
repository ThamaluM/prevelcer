# users/urls.py

from django.conf.urls import url
from users.views import dashboard
from users.views import register

urlpatterns = [
    url("dashboard/", dashboard, name="dashboard"),
    url("register/",register, name="register"),
]