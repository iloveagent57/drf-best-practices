from rest_framework import serializers
from .base_serializers import ReadOnlyModelSerializer
from tutorial.quickstart.models import Article


class ArticleReadOnlySerializer(ReadOnlyModelSerializer):
    """
    Article serializer
    """
    class Meta:
        model = Article
        fields = '__all__'


class ArticleReadWriteSerializer(serializers.ModelSerializer):
    """
    Article read-write serializer.
    """
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['id']
