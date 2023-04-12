from rest_framework import serializers
from .base_serializers import ReadOnlyModelSerializer
from tutorial.quickstart.models import Publication
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer


class PublicationArticleSerializer(NestedHyperlinkedModelSerializer):
    """
    https://github.com/alanjds/drf-nested-routers#hyperlinks-for-nested-resources
    """
    parent_lookup_kwargs = {
        'publication_pk': 'publication__pk',
    }
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationReadOnlySerializer(serializers.ModelSerializer):
    """
    Publication read-only serializer.

    """
    class Meta:
        model = Publication
        fields = '__all__'

    # articles = PublicationArticleSerializer(many=True, read_only=True)


class PublicationReadWriteSerializer(serializers.ModelSerializer):
    """
    Publication read-write serializer.
    """
    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ['id']
