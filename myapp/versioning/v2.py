from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileViewV2(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "name": "man",
            "aadhaar_number": "1234-5678-9012"
        })
