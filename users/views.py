from rest_framework import viewsets, generics, authentication, permissions
from .models import User
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# TODO: make UserViewSet only accesible by admin in production


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # make sure anonym Users can not access /users in production
    # permission_classes = [
    #     permissions.DjangoModelPermissions, permissions.IsAuthenticated]

# accessible by anyone to create user


class CreateUserView(generics.CreateAPIView):
    """Create new user in system"""
    serializer_class = UserSerializer


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
