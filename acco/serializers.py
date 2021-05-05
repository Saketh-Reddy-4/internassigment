from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
from django.contrib.auth.models import Group
from . models import Advisior

class AdvisiorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisior
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','time')

class GroupBSerializer(serializers.ModelSerializer):
    adv = AdvisiorSerializer();
    usr = UserSerializer();
    class Meta:
        model = Group
        fields = ('id','time','adv','usr')
