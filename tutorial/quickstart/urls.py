from django.urls import include, path

urlpatterns = [
    path('api/', include('tutorial.quickstart.api.urls')),
]
