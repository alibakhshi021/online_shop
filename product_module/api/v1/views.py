from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerializers
from ...models import Product
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


# @api_view(["GET", "POST"])
# @permission_classes([IsAdminUser])
# def product_view(request):
#     if request.method == "GET":
#         products = Product.objects.filter(is_active=True)
#         serializer = ProductSerializers(products, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = ProductSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class ProductList(APIView):
    """getting a list of post and creating new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers

    def get(self,request):
        """retrieving a lis of posts"""
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """creating a post whit provided data"""
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        





# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([AllowAny])
# def detail_view(request, id):
#     product = get_object_or_404(Product,pk=id, is_active=True)
#     if request.method == "GET":
#         serializer = ProductSerializers(product)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = ProductSerializers(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == "DELETE":
#         product.delete()
#         return Response({"detail" : "item remove successfully"})


class ProductDetail(APIView):
    """getting of the posts and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers

    def get(self, request, id):
        """removing posts data """
        product = get_object_or_404(Product,pk=id, is_active=True)
        serializer = self.serializer_class(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        """editing the post data"""
        product = get_object_or_404(Product,pk=id, is_active=True)
        serializer = ProductSerializers(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        """deleting the post object"""
        product = get_object_or_404(Product, pk=id, status=True)
        product.delete()
        return Response({"detail" : "item remove successfully"}), status.HTTP_204_NO_CONTENT
