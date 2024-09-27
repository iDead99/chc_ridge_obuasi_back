from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from . models import Member
from rest_framework.serializers import ModelSerializer

# class UserCreateSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         fields = ['id', 'first_name', 'last_name',
#                   'email', 'password', 'phone',
#                   'residence', 'gps_address', 'occupation']

# class UserSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ['id', 'first_name', 'last_name',
#                   'email', 'password', 'phone',
#                   'residence', 'gps_address', 'occupation']

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'id', 'first_name', 'last_name',
            'email', 'phone', 'residence',
            'gps_address', 'occupation'
        ]
