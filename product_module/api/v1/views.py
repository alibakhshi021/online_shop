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



class ProductListView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_classes = ProductSerializers
    queryset = Product.objects.filter(is_active=True)

    def list(self, request):
        serializer = self.serializer_classes(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_classes(product_object)
        return Response(serializer.data)
        
