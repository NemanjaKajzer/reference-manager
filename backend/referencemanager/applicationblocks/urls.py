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
    path('user/<str:pk>/', views.userProfilePage, name='user'),
    path('teams/', views.teamCreationPage, name='teams'),
    path('team/<str:pk>/', views.teamProfilePage, name='team'), 
    path('ranks/', views.rankCreationPage, name='ranks'),
    path('projects/', views.projectCreationPage, name='projects'),
    path('project/<str:pk>/', views.projectProfilePage, name='project'),
    path('reference/<str:pk>/', views.referenceProfilePage, name='reference'),
    #path('teams/<str:pk>/', views.teamCreationPage, name='teams'),        view ----> def teamCreationPage(request, pk)     team = Team.objects.get(id=pk)
]