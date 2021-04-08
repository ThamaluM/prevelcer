from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


from .serializers import UserSerializer, ProfileSerializer,FriendRequestSerializer, RiskScaleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User,Group
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics



from friend_requests.models import FriendRequest
from pressure_data.models import Mattress
from risk_assessment.models import RiskScale

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
    #permission_classes = [IsAdminUser]

    def get(self,request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=ValueError):
    #         serializer.create(validated_data=request.data)
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_201_CREATED
    #         )
    #     return Response(
    #         {
    #             "error": True,
    #             "error_msg": serializer.error_messages,
    #         },
    #         status=status.HTTP_400_BAD_REQUEST
    #     )

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_account(request):
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


class ProfileRecordView(APIView):
    def get(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(user=request.user,validated_data=request.data)
            roles = ['Admin','Patient','Carer','Doctor']
            group = Group.objects.get(name=roles[request.user.profile.role])
            request.user.groups.set([group])
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



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class MemberListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        role = self.kwargs['role']
        return User.objects.filter(groups__name=role)



class FriendRequestView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        request_set = FriendRequest.objects.filter(receiver=request.user,status=0)
        serializer = FriendRequestSerializer(request_set,many=True)
        return Response(serializer.data)

    def post(self,request):
        Sent = 0 
        receiver  = User.objects.get(username=request.data["receiver"])
        request.data["receiver"] = receiver.pk
        request.data["status"] = Sent
        request.data["sender"] = request.user.pk
        request.data["sender_name"] = request.user.username
        request.data["receiver_name"] = receiver.username
        serializer = FriendRequestSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=ValueError):
            #serializer.update(sender=request.user,status=Sent,receiver=receiver,validated_data=request.data)
            FriendRequest.objects.create(sender=request.user,receiver = receiver,status = Sent)
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

    def delete(self, request):

        sender = request.user
        receiver  = User.objects.get(username=request.data["receiver"])
        friend_request = None
        try:
            friend_request = FriendRequest.objects.get(sender=sender,receiver=receiver) 
        except:
            pass
        if friend_request:
            friend_request.delete() 
            return Response('Request Deleted')    
        else:
            sender, receiver = receiver, sender
            friend_request = FriendRequest.objects.get(sender=sender,receiver=receiver)
            return Response('Request Deleted')     


    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def show_requests_sent(request):
    
    request_set = FriendRequest.objects.filter(sender=request.user,status=0)
    serializer = FriendRequestSerializer(request_set,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def accept_friend_request(request):
    friend_request = FriendRequest.objects.get(receiver=request.user,id=request.data["id"])
    request.user.profile.friends.add(friend_request.sender)
    friend_request.sender.profile.friends.add(request.user)
    accepted = 1
    friend_request.status = accepted
    friend_request.save()
    return Response(friend_request.sender.username + " is added to the friend list.")


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def show_friends(request):
    serializer = UserSerializer(request.user.profile.friends,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def show_connections(request,role):

    #role = self.kwargs['role']
        
    serializer = UserSerializer(request.user.profile.friends.filter(groups__name=role),many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def unfriend(request):
    friend = User.objects.get(username=request.data["username"])
    request.user.profile.friends.remove(friend)
    friend_request = None
    try:
        friend_request = FriendRequest.objects.get(receiver=request.user,sender=friend)
    except:
        pass
    if not friend_request:
        friend_request = FriendRequest.objects.get(receiver=friend,sender=request.user)
    friend_request.delete()
    return Response(request.data["username"]+" unfriended.")

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def register_mat(request):

    mat = Mattress.objects.create(patient=request.user,serial=request.GET["serial"].strip())
    return JsonResponse({"serial":mat.serial})



class RiskScaleView(APIView):

    queryset = RiskScale.objects.all()
    serializer_class = RiskScaleSerializer
    permission_classes = [permissions.IsAuthenticated]
    #http_method_names = ['get', 'post']

    def get(self,request):
        
        if request.user.username == request.GET["patient"]:
            patient = request.user
        else:
            patient = request.user.profile.friends.get(username=request.GET["patient"])

        serializer = RiskScaleSerializer(patient.risk_scale)

        return Response(serializer.data)

    
    def post(self,request):

        if request.user.profile.role == 2:
            
            request.data["assessed_by"] = request.user.pk

            serializer = RiskScaleSerializer(data=request.data)

            if serializer.is_valid(raise_exception=ValueError):
                #serializer.update(sender=request.user,status=Sent,receiver=receiver,validated_data=request.data)
                RiskScale.objects.create(**request.data)
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

        else:
            return Response({"error":"A doctor is needed to fill this"})
            


    

        




