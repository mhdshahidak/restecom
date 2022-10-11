
from django_filters.rest_framework import FilterSet
from mosh.models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields ={
            'collection_id':['exact'],
            'max_offer_price':['gt','lt']
        }