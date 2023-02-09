from rest_framework import viewsets, generics, authentication, permissions
from .models import User, UserProfile
from .serializers import (UserSerializer, UserProfileSerializer,
                          AuthTokenSerializer)
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response

# TODO: make UserViewSet only accesible by admin in production


class UserViewSet(viewsets.ModelViewSet):
    """Allows unauthenticated users to create
    a new user, but requires authentication to retrieve, update, delete"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get', 'put', 'patch', 'delete'])
    def userprofile(self, request, pk=None):
        user = self.get_object()
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if request.method in ['PUT', 'PATCH']:
            serializer = UserProfileSerializer(
                user_profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status="400")

        if request.method == 'DELETE':
            user_profile.delete()
            return Response(status="204")

        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

# accessible by anyone to create user


# class CreateUserView(generics.CreateAPIView):
#     """Create new user in system"""
#     serializer_class = UserSerializer


# email and pw needed to get auth token
class CreateTokenView(ObtainAuthToken):
    """Create auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    # user must be authenticated to use this API
    permission_classes = [permissions.IsAuthenticated]

    # retrieve user that is attached to the request, get_object calls serializer
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer

#     permission_classes = [
#         permissions.DjangoModelPermissions, permissions.IsAuthenticated]

#     @action(detail=True, methods=['get'])
#     def user(self, request, pk=None):
#         user_profile = self.get_object()
#         user = user_profile.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
