
from rest_framework import serializers




class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    name=serializers.CharField(max_length=225)
    # price=serializers.DecimalField(max_digits=6,decimal_places=2)