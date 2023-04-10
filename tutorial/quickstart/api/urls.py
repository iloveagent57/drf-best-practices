from django.urls import include, path

urlpatterns = [
    path('v1/', include('tutorial.quickstart.api.v1.urls')),
]
