from django.conf.urls import url, include
from rest_framework import routers
from referencemanager.applicationblocks import views
from django.urls import path

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]