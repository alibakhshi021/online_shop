from rest_framework import serializers
from ...models import Product
# class Product_serializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=250)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"