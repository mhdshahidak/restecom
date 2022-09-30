from rest_framework import serializers
from . models import Product,Collection


# for nested relation
class CollectionSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    category=serializers.CharField(max_length=225)





class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    name=serializers.CharField(max_length=225)
    max_offer_price=serializers.FloatField()

    # price is not in  modal Product we made a function to it
    price=serializers.SerializerMethodField(method_name="calculate")
    def calculate(self, product: Product):
        return product.max_offer_price *1.1  

    #1st method how to add forigenkey in  where it gives an id of the collection
    # collection =serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    #2nd method how to add forigenkey in  where it gives an string name of the fk
    # collection =serializers.StringRelatedField()

    #3rd how to add in nested object
    # collection = CollectionSerializer()

    #4rd how to redirect to an endpoint
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name="collection-detail"
    )



    # # validation
    #     def validate(self,data):
    #         if data['password'] !=data['conform_password']:
    #             return serializers,ValueError('passmust be same')
    #         return(data)





# modal serilizer it is used because of when we make chnage in model we should also change in serilizser to avoid this
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','name','max_offer_price','collection']
        # or
        # fields ='__all__'

    # # to create a data    
    # def create(self, validated_data):
    #     product=Product(**validated_data)
    #     product.other=1
    #     product.save()
    #     return product

    # # to update
    # def update(self, instance, validated_data):
    #     instance.name=validated_data.get('name')
    #     instance.save()
    #     return instance

        



class ExeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields =['id','category','count']
        count= serializers.IntegerField()



