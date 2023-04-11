from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from ...quickstart.models import Article
from ..serializers import ArticleReadOnlySerializer, ArticleReadWriteSerializer
from .base_views import CreateUpdateModelMixin, RetrieveListModelMixin


class ArticleReadOnlyViewSet(RetrieveListModelMixin):
    """
    Viewset mixin that allows articles to be listed or retrieved.
    """


class ArticleCreateUpdateViewSet(CreateUpdateModelMixin):
    """
    Viewset mixin that allows articles to be created or updated.
    """


class ArticleViewSet(
    ArticleReadOnlyViewSet,
    ArticleCreateUpdateViewSet,
    viewsets.GenericViewSet,
):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ArticleReadWriteSerializer
        return ArticleReadOnlySerializer
