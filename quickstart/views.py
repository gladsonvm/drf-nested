from django.shortcuts import render
from quickstart.models import UserProfile, nestedmodel
# Create your views here.
from django.core import serializers
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, UserProfileSerializer, NestedSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin
import json
from rest_framework.response import Response
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class NestedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = nestedmodel.objects.all()
    serializer_class = NestedSerializer
    def create(self, request, *args, **kwargs):
        info = request.DATA['info']
        user = User.objects.get(username=request.DATA['user']['username'])
        print user
        profile = UserProfile.objects.get(user=user)
        print profile
        nst = nestedmodel.objects.create(info=info, user=user, profile=profile)
        serialized_obj = serializers.serialize('json', [ nst, ])
        json_serialized = json.loads(serialized_obj)
        data = json.dumps(json_serialized[0])
        print data,'\n\n\n::::'
        # return HttpResponse(data)
        # import ipdb;ipdb.set_trace();
        # print Response(nst)
        return Response(json_serialized)
        # import ipdb;ipdb.set_trace();

class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter