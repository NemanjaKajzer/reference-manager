from django.conf.urls import url, include
from rest_framework import routers
from referencemanager.applicationblocks import views
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path('upload/', views.upload, name='upload'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('teams/', views.teamCreationPage, name='teams'),
    path('ranks/', views.rankCreationPage, name='ranks'),
]