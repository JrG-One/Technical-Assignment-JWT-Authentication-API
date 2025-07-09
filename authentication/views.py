from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.settings import api_settings

class TokenVerifyView(APIView):
    """
    POST { "token": "<your JWT here>" }
    → returns 200 + {"valid": true} if valid, 401 if not.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        token = request.data.get('token')
        try:
            backend = TokenBackend(
                algorithm=api_settings.ALGORITHM,
                signing_key=api_settings.SIGNING_KEY,
                verifying_key=api_settings.VERIFYING_KEY,
            )
            backend.decode(token, verify=True)
            return Response({'valid': True})
        except (TokenError, InvalidToken):
            return Response({'valid': False}, status=status.HTTP_401_UNAUTHORIZED)


class ValidateTokenView(APIView):
    """
    GET with Authorization: Bearer <access token>
    → returns user info & expiry timestamp.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        token = request.auth  # the raw token string
        backend = TokenBackend(
            algorithm=api_settings.ALGORITHM,
            signing_key=api_settings.SIGNING_KEY,
            verifying_key=api_settings.VERIFYING_KEY,
        )
        data = backend.decode(token, verify=False)
        return Response({
            'valid': True,
            'user': user.username,
            'expires': data.get('exp'),
        })
