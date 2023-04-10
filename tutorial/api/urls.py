from django.urls import include, path

urlpatterns = [
    path('v1/', include('tutorial.api.v1.urls')),
]
