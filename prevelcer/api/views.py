from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to our home page </h1>  <b> Let us prevent pressure ulcers. <b>Prevention is better than cure.</b>") #"Hello Welcome"

def test_get(request):
    return JsonResponse({"topic":"just_testing","message":"Hi this is really cool."})






class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )