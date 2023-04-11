from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from edx_rbac.utils import get_decoded_jwt_from_auth


class UserJwtView(APIView):
    """
    View to get a user's decoded JWT and return it in the response payload.
    Never do this in production
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a user's decoded jwt token.
        """
        edx_decoded = get_decoded_jwt_from_auth(request)
        return Response({
            'simplejwt': request.auth.payload,
            'edxjwt': edx_decoded,
        })
