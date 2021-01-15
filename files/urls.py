from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import  MainModelViewSet

router = DefaultRouter()
router.register('MainModel',MainModelViewSet, basename="api")


urlpatterns = [
    path('api/',include(router.urls) ),
]