from django.contrib.auth.models import User
from rest_framework import viewsets
from referencemanager.applicationblocks.serializers import UserSerializer, ReferenceSerializer
from .models import Reference

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reference.objects.all().order_by('-id')
    serializer_class = ReferenceSerializer
