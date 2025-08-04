from rest_framework import generics
from djangoProject import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model, authenticate
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404

# from django.core.mail import send_mail
from mail_templated import send_mail, EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError, DecodeError
from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    CustomTokenObtainPairSerializer,
    ChangePassApiSerializer,
    ProfileApiSerializer,
    ActivationResendSerializer,
)
from ..utils import EmailTreading
from ...models import User, Profile


# Registration
class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_token_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "admin@admin.com",
                to=[email],
            )
            EmailTreading(email_obj).start()

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


# Login
User = get_user_model()


class LoginAPIView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=401)

        if not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=401)

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.id,
                "email": user.email,
            }
        )


# logout
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Logged out successfully."}, status=200)


# create JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePassApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePassApiSerializer

    def get_object(self):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # set_password also hashed the password that the yser will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"detail": "password change successful"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileApiSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class TestEmailView(APIView):
    def get(self, request, *args, **kwargs):
        self.email = "nima.davari021@gmail.com"
        user_obj = get_object_or_404(User, email=self.email)
        token = self.get_token_for_user(user_obj)

        email_obj = EmailMessage(
            "email/hello.tpl", {"token": token}, "admin@admin.com", to=[self.email]
        )
        EmailTreading(email_obj).start()
        return Response("Test-Email")

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get("user_id")
        except jwt.ExpiredSignatureError:
            return Response(
                {"detail": "token has been expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except DecodeError:
            return Response(
                {"detail": "token is not valid"}, status=status.HTTP_400_BAD_REQUEST
            )

        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response({"detail": "Your account has already been verified"})
        user_obj.is_verified = True
        user_obj.save()

        print(token)
        return Response(
            {"detail": "your account has been verified and activate successful"}
        )


class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ActivationResendSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActivationResendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_token_for_user(user_obj)
        email_obj = EmailMessage(
            "email/hello.tpl", {"token": token}, "admin@admin.com", to=["email"]
        )
        EmailTreading(email_obj).start()
        return Response(
            {"detail": "user activation resend successfully"}, status=status.HTTP_200_OK
        )

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
