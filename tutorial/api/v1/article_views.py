from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, status, viewsets
from edx_rbac.mixins import PermissionRequiredMixin
from ...quickstart.models import Article
from ..serializers import ArticleReadOnlySerializer, ArticleReadWriteSerializer
from .base_views import CreateUpdateModelMixin, RetrieveListModelMixin
from .schema import ARTICLE_VIEWSET_SCHEMA


class ArticleReadOnlyViewSet(RetrieveListModelMixin):
    """
    Viewset mixin that allows articles to be listed or retrieved.
    """


class ArticleCreateUpdateViewSet(CreateUpdateModelMixin):
    """
    Viewset mixin that allows articles to be created or updated.
    """


@extend_schema(
    tags=['articles'],
)
@extend_schema_view(**ARTICLE_VIEWSET_SCHEMA)
class ArticleViewSet(
    PermissionRequiredMixin,
    ArticleReadOnlyViewSet,
    ArticleCreateUpdateViewSet,
    viewsets.GenericViewSet,
):
    """
    Read, list, create, and update actions for Articles.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.select_related('publication').filter(
            publication=self.kwargs['publication_pk']
        )

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ArticleReadWriteSerializer
        return ArticleReadOnlySerializer

    def get_permission_required(self):
        if self.action in ['create', 'update']:
            return ['articles.can_write']
        return ['articles.can_read']

    def get_permission_object(self):
        return self.kwargs.get('publication_pk')
