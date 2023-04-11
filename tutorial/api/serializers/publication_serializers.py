from rest_framework import serializers
from .base_serializers import ReadOnlyModelSerializer
from tutorial.quickstart.models import Publication


class PublicationReadOnlySerializer(ReadOnlyModelSerializer):
    """
    Publication read-only serializer.
    """
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationReadWriteSerializer(serializers.ModelSerializer):
    """
    Publication read-write serializer.
    """
    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ['id']
