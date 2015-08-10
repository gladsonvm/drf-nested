__author__ = 'gladson'
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import UserProfile, nestedmodel




class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        user = UserSerializer()
        fields = ('user', )

    def create(self, validated_data):
        import ipdb;ipdb.set_trace();

class NestedSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer()
    user = UserSerializer()
    class Meta:
        model = nestedmodel
        fields = ('info', 'user', 'profile')