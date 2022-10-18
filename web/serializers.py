

from rest_framework import serializers
from mosh.models import Review,Product,Collection
from shoping.models import CartItems,OrderItem,Cart
from django.db import transaction
# djosher series
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


       
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields=['id','date','name','description','product']
            # forgin key adding through url

        fields=['id','date','name','description']  
    def create(self, validated_data):
        product_id= self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','username','password','email','first_name','last_name']


# --------------------------------------------

class CollectionOrdrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','name','buying_price','qty','collection']


class OrdrtSerializer(serializers.ModelSerializer):
    collection = CollectionOrdrtSerializer(many=True)
    class Meta:

        model = Collection
        fields=['id','category','collection']


class CreateOrdrtSerializer(serializers.Serializer):  
    cart_id=serializers.UUIDField()   

    def validate_cart_id(self,cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('no cart with that id ')
        if CartItems.objects.filter(cart_id=cart_id).count()==0:
            raise serializers.ValidationError('The Cart is Empty ')

        return cart_id    

    def save(self, **kwargs):
        # it is an set ofcode when suddenly error occur in any procec no code will exicuted
        with transaction.atomic():
            print(self.validated_data['cart_id'])
            print( self.context['user_id'])
            order=Collection.objects.get(user_id=self.context['user_id'])
            cartitem=CartItems.objects.select_related('product').filter(cart_id=self.validated_data['cart_id'])
            oederItem=[
                OrderItem(
                order=order,
                product=item.product,
                price=item.product.max_offer_price,
            ) for item in cartitem]
            OrderItem.objects.bulk_create(oederItem)
            Cart.objects.filter(pk=self.validated_data['cart_id']).delete()


            return order

class UpdateOrdrtSerializer(serializers.Serializer):  
    class Meta:
        model = Product
        fields=['buying_price']
            
