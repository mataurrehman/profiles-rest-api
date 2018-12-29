from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status
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