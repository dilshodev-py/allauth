from rest_framework.fields import EmailField
from rest_framework.serializers import Serializer


class ResetPasswordSerializer(Serializer):
    email = EmailField()