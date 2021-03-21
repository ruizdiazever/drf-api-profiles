from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ I serialize a field to test our APIView """

    name = serializers.CharField(max_length=10)