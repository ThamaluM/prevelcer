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
from .views import UserRecordView,ProfileRecordView,UserViewSet,FriendRequestView, MemberListView, RiskScaleView
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all_users', views.UserViewSet)



app_name = 'api'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('get/',views.test_get,name = 'test_get'),
    path('user/', UserRecordView.as_view(), name='users'),
    path('register/',views.create_account,name="create_account"),
    path('profile/', ProfileRecordView.as_view(), name='users'),
    path('friend_request/',FriendRequestView.as_view(), name = 'friend_requests'),
    path('outgoing_requests/',views.show_requests_sent,name = 'outgoing_requests'),
    path('accept_request/',views.accept_friend_request,name = 'accept_request'),
    path('show_friends/',views.show_friends,name='show_friend_list'),
    path('show_connections/<str:role>',views.show_connections,name='show_friend_list_by_roles'),
    path('unfriend/',views.unfriend,name='unfriend'),
    path('risk', RiskScaleView.as_view({'post': 'update_or_create'}), name = 'risk_assessment'),
    path('registermat',views.register_mat, name = 'register_mat'),
    path('device', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('community/<str:role>', MemberListView.as_view(), name = 'group_wise_user_listing'),
    path('', include(router.urls)),
]






