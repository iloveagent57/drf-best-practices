from django.urls import include, path
# from rest_framework import routers
from rest_framework_nested import routers
from tutorial.api.v1 import (
    ArticleViewSet,
    PublicationViewSet,
    UserViewSet,
    GroupViewSet,
    UserJwtView,
)

# Cruft from DRF standard tutorial
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

# https://www.django-rest-framework.org/api-guide/routers/#usage
router = routers.SimpleRouter()
router.register(r'publications', PublicationViewSet)

publications_router = routers.NestedSimpleRouter(
    router,
    r'publications',
    lookup='publication',
)
# Now register the "sub-router" for articles
publications_router.register(
    r'articles',
    ArticleViewSet,
    basename='publication-article',
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include(publications_router.urls)),
    path('user-jwt', UserJwtView.as_view(), name='user-jwt-get'),
]
