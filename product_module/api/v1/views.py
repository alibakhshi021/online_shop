from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import Product_serializers
from ...models import Product

@api_view()
@permission_classes([AllowAny])
def product_view(request):
    return Response("ok")

@api_view()
@permission_classes([AllowAny])
def detail_view(request, id):
    try:
        product = Product.objects.get(pk=id)
        serializers = Product_serializers(product)
        return Response(serializers.data)
    except:
        return Response("{'detail is not found'}", status=404)