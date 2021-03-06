from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from django_tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    
    API endpoint that allows users to be viewed or edited
     
    """
    permission_classes = (permissions.IsAuthenticated,)

    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    
    API endpoint that allows Groups to be viewed or edited
     
    """
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
