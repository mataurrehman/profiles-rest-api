from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test API View"""

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
