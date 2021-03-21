from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ API View of test """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list features of APIView """
        an_apiview = [
            'We use HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar with a traditional view of Django',
            'It gives us greater control over the logic of our application',
            'Is manually mapped to the URLs',
        ]

        """ When we have a 'get' we have to return a 'response'. This can be as a list or dictionary."""
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Make a message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Manages to update an object. When we update an object we must also update the object's ID."""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Manage to partial update of an object. """
        return Response({'method':'PATH'})

    def delete(self, request, pk=None):
        """ Delete an object. """
        return Response({'method':'DELETE'})
