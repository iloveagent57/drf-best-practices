from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ReadOnlyModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    https://www.django-rest-framework.org/api-guide/serializers/#read-only-baseserializer-classes

    To implement a read-only serializer using the BaseSerializer class,
    we just need to override the .to_representation() method.

    https://testdriven.io/blog/drf-serializers/
    "If your serializers contain a lot of nested data,
    which is not required for write operations,
    you can boost your API performance by creating separate read and write serializers."

    Inspired by
    https://stackoverflow.com/a/52467796
    """
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields

    def to_internal_value(self, data):
        raise NotImplementedError


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
