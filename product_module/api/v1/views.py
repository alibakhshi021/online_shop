from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view()
@permission_classes([AllowAny])
def product_view(request):
    return Response("ok")

@api_view()
@permission_classes([AllowAny])
def detail_view(request, id):
    return Response(id)