from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from authentication.models import User
from authentication.serializers import UserSerializer
from authentication.permission import IsLoggedInUserOrAdmin


from authentication.permission import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['post'], detail=True, permission_classes=[IsLoggedInUserOrAdmin],
        url_path='change-password', url_name='change_password')
        
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]