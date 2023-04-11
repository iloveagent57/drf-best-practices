"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


spectacular_view = SpectacularAPIView(
    api_version='v1',
    title='my-title-here',
)

spec_swagger_view = SpectacularSwaggerView()

spec_redoc_view = SpectacularRedocView(
    title='Redoc view for the enterprise-subsidy API.',
    url_name='schema',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tutorial.api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', spectacular_view.as_view(), name='schema'),
    path('api/schema/swagger-ui/', spec_swagger_view.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', spec_redoc_view.as_view(url_name='schema'), name='redoc'),
]
