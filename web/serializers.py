

from rest_framework import serializers
from mosh.models import Review



       
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields=['id','date','name','description','product']
            # forgin key adding through url

        fields=['id','date','name','description']  
    def create(self, validated_data):
        product_id= self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)