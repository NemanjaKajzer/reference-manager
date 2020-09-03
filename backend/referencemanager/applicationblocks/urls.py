from django.conf.urls import url, include
from rest_framework import routers
from referencemanager.applicationblocks import views
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/<str:pk>/', views.userProfilePage, name='user'),
    path('teams/', views.teamCreationPage, name='teams'),
    path('team/<str:pk>/', views.teamProfilePage, name='team'),
    path('delete_team/<str:pk>/', views.deleteTeam, name='delete_team'),
    path('ranks/', views.rankCreationPage, name='ranks'),
    path('rank/<str:pk>/', views.rankProfilePage, name='rank'),
    path('delete_rank/<str:pk>/', views.deleteRank, name='delete_rank'),
    path('projects/', views.projectCreationPage, name='projects'),
    path('project/<str:pk>/', views.projectProfilePage, name='project'),
    path('delete_project/<str:pk>/', views.deleteProject, name='delete_project'),
    path('references/', views.referenceCreationPage, name='references'),
    path('reference/<str:pk>/', views.referenceProfilePage, name='reference'),
    path('delete_reference/<str:pk>/', views.deleteReference, name='delete_reference'),
    path('forbidden/', views.forbidden, name='forbidden'),
]