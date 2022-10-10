
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import Collection, Employee, Items, Product,Review
from rest_framework import permissions
from common.models import User
from django.contrib.auth import get_user_model,authenticate


# for nested relation
class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = serializers.CharField(max_length=225)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=225)
    max_offer_price = serializers.FloatField()

    # price is not in  modal Product we made a function to it
    price = serializers.SerializerMethodField(method_name="calculate")

    def calculate(self, product: Product):
        return product.max_offer_price * 1.1

    # 1st method how to add forigenkey in  where it gives an id of the collection
    # collection =serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # 2nd method how to add forigenkey in  where it gives an string name of the fk
    # collection =serializers.StringRelatedField()

    # 3rd how to add in nested object
    # collection = CollectionSerializer()

    # 4rd how to redirect to an endpoint
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name="collection-detail"
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
        fields = ["id", "name", "max_offer_price", "collection"]
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
        fields = ["id", "category", "count"]
        count = serializers.IntegerField()




class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
    def create(self, validated_data):
        user = Employee.objects.create(
            username=validated_data["username"],
            password=validated_data["password"],
            phone=validated_data["phone"],
            name=validated_data["name"],
        )
        user.save()
        return user






class EmployeeRegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     write_only=True, required=True, validators=[validate_password]
    # )
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            # "password2",
            "first_name",
            "last_name",
            "email",
        )

    # def validate(self, attrs):
    #     if attrs["password"] != attrs["password2"]:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."}
    #         )
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        user.is_staff=True
        user.set_password(validated_data["password"])
        user.save()
        return user



        
class AddItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"
    # emp= request.employee.id
    def get(self,request):
        print(self.request.user.id,'*'*20)    
    def create(self, validated_data):
        item = Items.objects.create(
            name=validated_data["name"],
            category=validated_data["category"],
            value=validated_data["value"],
        )   
        item.save()
        return item
    
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields=['id','date','name','description','product']
            # forgin key adding through url

        fields=['id','date','name','description']  
    def create(self, validated_data):
        product_id= self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)