from django.forms import ValidationError
from rest_framework import viewsets, generics, authentication, permissions
from .models import User, UserProfile
from .serializers import (UserSerializer, UserProfileSerializer,
                          AuthTokenSerializer)
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from django.conf import settings
# from django.http import HttpResponse
# from django.views.static import serve


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_authenticators(self):
        if self.request == 'POST':
            authentication_classes = []
        else:
            authentication_classes = [authentication.TokenAuthentication]
        return [authenticator() for authenticator in authentication_classes]

    @action(detail=True, methods=['get', 'post', 'put', 'patch', 'delete'])
    def userprofile(self, request, pk=None):
        user = self.get_object()
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if request.method in ['PUT', 'PATCH', 'POST']:
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


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    # user must be authenticated to use this API
    permission_classes = [permissions.IsAuthenticated]

    # retrieve user that is attached to the request, get_object calls serializer
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response(e.message, status='400')


class CustomAuthToken(ObtainAuthToken):
    """Override standard token return, to also return userid"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.id
        })


# commented out, since I decided to include the ProfileData in the UserViewSet
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

# commented out since I used external image API for now
# class UserImageView(APIView):
#     """GET endpoint to retrieve userimages that have been uploaded"""
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         file_path = kwargs.get('file_path', '')
#         response = serve(request, file_path, document_root=settings.MEDIA_ROOT)
#         if not response:
#             return HttpResponse(status=404)
#         return response

# email and pw needed to get auth token
