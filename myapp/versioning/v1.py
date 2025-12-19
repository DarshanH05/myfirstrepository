from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileViewV1(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "name": "man",
            "age": 23
        })
