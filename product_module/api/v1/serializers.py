from rest_framework import serializers

class Product_serializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
