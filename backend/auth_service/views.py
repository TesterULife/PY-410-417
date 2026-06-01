from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class TestJWTView(APIView):
    authentication_classes = [
        SessionAuthentication,
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        return Response({
            'message': 'Доступ разрешен',
            'user': request.user.username,
        })