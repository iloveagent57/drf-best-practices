from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, permissions, status, viewsets, response
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


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    """
    Class for listing or creating articles within a publication.

    We'll try to make this nested in the router, with a path like
    /api/v1/publications/{publication_pk}/articles/

    Permission concepts to implement:
    - To _create_ an article within a publication, I must be an admin in the publication.
    - To _list_ an article within a publication, I must be a user in the article's publication
      _and_ be the author of the article (I realize that's a little silly).
    """
    @property
    def publication_pk(self):
        return self.kwargs['publication_pk']

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleReadWriteSerializer
        return ArticleReadOnlySerializer

    def get_queryset(self):
        """
        https://www.django-rest-framework.org/api-guide/generic-views/#get_querysetself

        Returns the queryset that should be used for list views, and that should be used as the base for
        lookups in detail views. Defaults to returning the queryset specified by the queryset attribute.
        This method should always be used rather than accessing self.queryset directly,
        as self.queryset gets evaluated only once, and those results are cached for all subsequent requests.
        May be overridden to provide dynamic behavior, such as returning a queryset,
        that is specific to the user making the request.
        """
        return Article.objects.select_related('publication').filter(
            publication=self.publication_pk,
        )

    def list(self, request, publication_pk):
        queryset = self.get_queryset().filter(
            author=request.user,
        )
        serializer = self.get_serializer_class()(queryset, many=True)
        return response.Response(serializer.data)
