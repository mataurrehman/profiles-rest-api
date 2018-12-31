from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from .import permissions

# Create your views here.

class HelloApiView(APIView):
    """ Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        :param request:
        :param format:
        :return a list of api view features:
        """
        an_apiview = [
            'uses hhtp methods as function (get,post,patch,put,delete)',
            'It is similar to traditional django view',
            'gives you most control over logic',
            'is mapped normally to URLS'
        ]
        return Response({'message': 'Hello', 'an_apiview' : an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API viewset."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello message."""

        a_viewset = [
            'User actions(list, create, retrieve, update, partial_update)',
            'Authomatically maps to url using Router',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by ID."""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles partially updating an object."""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile."""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):

    """ checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ Use the ObtainAuthToken ApiView to validate and create a token"""

        return ObtainAuthToken().post(request)