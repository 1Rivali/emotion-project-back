from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from rest_framework.authentication import authenticate
from .serializer import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken


# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    @extend_schema(responses=AuthTokenSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "is_superuser": user.is_superuser,
            }
        )


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    )
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = (
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    )


class DeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
