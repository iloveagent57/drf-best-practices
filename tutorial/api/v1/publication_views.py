from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from ...quickstart.models import Publication
from ..serializers import PublicationReadOnlySerializer, PublicationReadWriteSerializer
from .base_views import CreateUpdateModelMixin, RetrieveListModelMixin


class PublicationReadOnlyViewSet(RetrieveListModelMixin):
    """
    Viewset mixin that allows publications to be listed or retrieved.
    """


class PublicationCreateUpdateViewSet(CreateUpdateModelMixin):
    """
    Viewset mixin that allows publications to be created or updated.
    """


class PublicationViewSet(
    PublicationReadOnlyViewSet,
    PublicationCreateUpdateViewSet,
    viewsets.GenericViewSet,
):
    """
    API for reading and writing Publications.

    https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions
    """
    queryset = Publication.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PublicationReadWriteSerializer
        return PublicationReadOnlySerializer
