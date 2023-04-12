from drf_spectacular.utils import extend_schema
from rest_framework import status
from ..serializers import ArticleReadOnlySerializer, ArticleReadWriteSerializer


ARTICLE_VIEWSET_SCHEMA = {
    'retrieve': extend_schema(responses={
        status.HTTP_200_OK: ArticleReadOnlySerializer,
        status.HTTP_404_NOT_FOUND: None,
    }),
    'list': extend_schema(responses={
        status.HTTP_200_OK: ArticleReadOnlySerializer,
    }),
    'create': extend_schema(responses={
        status.HTTP_201_CREATED: ArticleReadWriteSerializer,
    }),
    'update': extend_schema(responses={
        status.HTTP_202_ACCEPTED: ArticleReadWriteSerializer,
    }),
    'partial_update': extend_schema(responses={
        status.HTTP_202_ACCEPTED: ArticleReadWriteSerializer,
    }),
}
