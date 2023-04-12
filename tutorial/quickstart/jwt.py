from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import PublicationMembership


class TokenWithRolesObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        memberships = PublicationMembership.objects.filter(user=user)

        # Add custom claims
        token['roles'] = [
            f'{membership.role}:{membership.publication_id}'
            for membership in memberships
        ]

        return token
