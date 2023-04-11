from django.urls import include, path
from rest_framework import routers
from tutorial.api.v1 import (
    ArticleViewSet,
    PublicationViewSet,
    UserViewSet,
    GroupViewSet,
    UserJwtView,
)

# https://www.django-rest-framework.org/api-guide/routers/#usage
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'publications', PublicationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('user-jwt', UserJwtView.as_view(), name='user-jwt-get'),
]
