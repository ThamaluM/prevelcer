# users/urls.py

from django.conf.urls import url
from users.views import dashboard
from rest_framework import routers
from users.views import register
from users import views
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url("dashboard/", dashboard, name="dashboard"),
    url("register/",register, name="register"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]