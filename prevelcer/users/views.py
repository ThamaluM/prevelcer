from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import Group
# import forms.UserForm as UserForm
# import forms.ProfileForm as Profile
from .forms import UserForm, ProfileForm

# Create your views here.

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("update_profile")
        else:
            #return messages.error(request,'Some error occured. Check the form again')
            return HttpResponse("User unavailable. Password mismatch or too short password.") #redirect('register')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            roles = ['Admin','Patient','Carer','Doctor']
            group = Group.objects.get(name=roles[request.user.profile.role])
            request.user.groups.set([group])
            return redirect('/user/dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):

        role = request.GET["role"]
        if role:
            queryset = User.objects.filter(groups__name=role)
        else:
            queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def test_auth(request):
    if request.user.is_authenticated:
        return HttpResponse("Hi. Successful.. This message is from Thamalu. You can see this if you have account.")
    else:
        return HttpResponse("Sorry. You have to create an account to see this.")


