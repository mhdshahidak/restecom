


from rest_framework import serializers
from mosh.serializers import ProductSerializer
from common.models import User
from .models import Cart, CartItems
from mosh.models import Product,Employee


class Simpleproductserializer(serializers.ModelSerializer):  
    class Meta:
        model = Product  
        fields = ['id','name','qty']



class CartItemserializer(serializers.ModelSerializer):     
    product = Simpleproductserializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self,cart_item:CartItems):

        print(cart_item.price,'&$$$$$$$$$$$$$$$$$$$$$$$$')
        print(cart_item.product.qty,'@@@@@@@@@@@@@@@@@@')
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
    product1 = Simpleproductserializer(many=True,read_only=True)
    
    
    # total_price = serializers.SerializerMethodField()

    # def get_total_price(self,cart_item:CartItems):
    #     # print(cart_item.price,'&$$$$$$$$$$$$$$$$$$$$$$$$')
    #     # print(cart_item.product__qty,'@@@@@@@@@@@@@@@@@@')
    #     return cart_item.price * cart_item.product1.qty

    class Meta:
        model = CartItems  
        fields = ['id','product1','price']



class AddCartItemsListerializer(serializers.ModelSerializer): 
    product_id= serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('no product Exist')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        price = self.validated_data['price']
        # print(cart_id,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(product_id,'**********************************************')
        # print(price,'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        try:  
            cart_item= CartItems.objects.get(cart_id=cart_id, product_id=product_id)
            # updating new item
            cart_item.price +=price
            cart_item.save()
            # from documentation
            self.instance=cart_item
        except CartItems.DoesNotExist:
            # crete new item
            # from documentation
            self.instance =CartItems.objects.create(cart_id=cart_id,product_id=product_id,price=price)
        return self.instance
    class Meta:
        model = CartItems  
        fields = ['id','product_id','price']   


class UpdateCartItemsListerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems  
        fields = ['price'] 


# djoser

class EmployeeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    # userobj=User.objects.get(id=user__id)
    class Meta:
        model = Employee
        fields=['id','user_id','phone','username']
    def create(self, validated_data):
        user = Employee.objects.create(
            phone=validated_data["phone"],
            username=validated_data["username"],
            user_id=validated_data["user_id"],
        )
        user.save()
        return user    
    