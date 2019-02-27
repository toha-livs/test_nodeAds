from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'elements', views.ElementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]