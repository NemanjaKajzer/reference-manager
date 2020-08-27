from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from referencemanager.applicationblocks import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('references', views.ReferenceViewSet)



urlpatterns = [
    url('refmng/', include('referencemanager.applicationblocks.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('refmng/upload/', views.upload)
]