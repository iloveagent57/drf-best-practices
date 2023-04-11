from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenWithRolesObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['roles'] = {}

        return token
