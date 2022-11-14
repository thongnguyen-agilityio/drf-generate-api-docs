from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'first_name', 'last_name']
        read_only_fields = ['first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PayeeSerializer(serializers.Serializer):
    speed = serializers.CharField(required=True, allow_blank=False, max_length=100)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    account_number = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    routing_number = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    account_type = serializers.CharField(
        required=False, allow_blank=True, max_length=100
    )
    type = serializers.CharField(required=False, allow_blank=True, max_length=100)


class RequestSerializer(serializers.Serializer):
    field1 = serializers.CharField(required=True, allow_blank=False, max_length=100)
    field2_test = serializers.CharField(required=True, allow_blank=False, max_length=100)
