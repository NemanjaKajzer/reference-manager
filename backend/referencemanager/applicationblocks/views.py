from django.contrib.auth.models import User
from rest_framework import viewsets
from referencemanager.applicationblocks.serializers import UserSerializer, ReferenceSerializer
from .models import Reference
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


@permission_classes((AllowAny,))
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ReferenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows references to be viewed or edited.
    """
    queryset = Reference.objects.all().order_by('-id')
    serializer_class = ReferenceSerializer
