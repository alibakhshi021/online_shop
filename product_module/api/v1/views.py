from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ProductSerializers
from ...models import Product
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def product_view(request):
    if request.method == "GET":
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
@permission_classes([AllowAny])
def detail_view(request, id):
    product = get_object_or_404(Product,pk=id, is_active=True)
    serializers = Product_serializers(product)
    return Response(serializers.data)