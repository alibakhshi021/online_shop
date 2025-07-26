from rest_framework import generics
from .serializers import (RegistrationSerializer, LoginSerializer,
                        CustomTokenObtainPairSerializer,ChangePassApiSerializer,
                        ProfileApiSerializer)
from rest_framework.response import Response
from rest_framework import status
from ...models import User, Profile
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


#Registration
class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                'email':serializer.validated_data['email']   
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Login
User = get_user_model()
class LoginAPIView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=401)

        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=401)

        token, _ = Token.objects.get_or_create(user=user)
    

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,

        })

#logout
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'detail': 'Logged out successfully.'}, status=200)
    
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
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            #check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            #set_password also hashed the password that the yser will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail': 'password change successful'}, status=status.HTTP_200_OK)
                            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ProfileApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileApiSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
    

class TestEmailView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        message = EmailMessage('email/hello.tpl', {'name': 'ali'}, 'admin@admin.com', to=['nima.davari021@gmail.com'])
        message.send()
        return Response('Test-Email')    