from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerializers
from ...models import Product
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets

class ProductList(ListCreateAPIView):
    """getting a list of post and creating new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers
    queryset = Product.objects.filter(is_active=True)


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """getting of the posts and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers
    queryset = Product.objects.filter(is_active=True)



class ProductListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_classes = ProductSerializers
    queryset = Product.objects.filter(is_active=True)

       
