from django.urls import path
from django.urls import include
from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
]