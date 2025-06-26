from rest_framework import generics
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from ...models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


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
    
# #TokenAuth    
class CustomAuthToken(ObtainAuthToken):
    # serializer_class = 
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }) 




# class LoginAPIView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 "token": token.key,
#                 "user_id": user.id,
#                 "email": user.email
#             })
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)