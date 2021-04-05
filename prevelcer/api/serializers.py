from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import Profile
from friend_requests.models import FriendRequest


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'role',
        )
        extra_kwargs = {}
        

    def update(self, user, validated_data):
        profile = user.profile
        for (key, value) in validated_data.items():
            setattr(profile, key, value)
        profile.save()
        
        return profile




class FriendRequestSerializer(serializers.ModelSerializer):

    sender_name = serializers.CharField(source="sender.username",blank=True,null=True) 
    receiver_name = serializers.CharField(source="receiver.username",blank=True,null=True)
    
    def create(self, validated_data):

        friend_request = FriendRequest.objects.create(**validated_data)
        return friend_request


    class Meta:
        model = FriendRequest
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=FriendRequest.objects.all(),
                fields=['sender', 'receiver']
            )
        ]
