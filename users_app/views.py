from datetime import timedelta

from rest_framework import status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users_app.models import UserAccounts
from users_app.serializers import UserSerializer, LoginSerializer, RegisterSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    print(UserSerializer(request.user).data)
    return Response(UserSerializer(request.user).data)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserAccounts.objects.all()

    http_method_names = ['get']
    permission_classes = (IsAdminUser, IsAuthenticated)
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserAccounts.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        user = UserAccounts.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, user)

        return user


class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        access_token.set_exp(lifetime=timedelta(minutes=30))

        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "token": str(access_token),
        }, status=status.HTTP_201_CREATED)


class RefreshViewSet(ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
