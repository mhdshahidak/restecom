
from asyncore import read
from rest_framework import serializers
from mosh.serializers import ProductSerializer
from .models import Cart, CartItems
from mosh.models import Product


class Simpleproductserializer(serializers.ModelSerializer):  
    class Meta:
        model = Product  
        fields = ['id','name','qty']



class CartItemserializer(serializers.ModelSerializer):     
    product = Simpleproductserializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self,cart_item:CartItems):
        # print(cart_item.price,'&$$$$$$$$$$$$$$$$$$$$$$$$')
        # print(cart_item.product.qty,'@@@@@@@@@@@@@@@@@@')
        return cart_item.price * cart_item.product.qty

    class Meta:
        model = CartItems  
        fields = ['id','product','price','total_price']


class Cartserializer(serializers.ModelSerializer):
    id= serializers.UUIDField(read_only=True)
    items = CartItemserializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField()
    def get_total_price(self,cart):
        return sum([item.price * item.product.qty for item in cart.items.all()])
    class Meta:
        model= Cart
        fields = ['id','productname','items','total_price']


class CartItemsListerializer(serializers.ModelSerializer):
    product = Simpleproductserializer(many=True,read_only=True)
    class Meta:
        model = CartItems  
        fields = ['id','product','price']