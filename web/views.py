from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from mosh.models import Collection, Employee, Product, Review
from .serializers import ReviewSerializer
from mosh.serializers import ProductSerializer, CollectionSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .pagination import DeafualtPagination

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    # filtering method1
#    ---------------------------------------------------------
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     collection_id = self.request.query_params.get('collection_id')
    #     if collection_id is not None:
    #         queryset=queryset.filter(collection_id=collection_id)
    #     return queryset


    # filtering method2   And seraching
#    ---------------------------------------------------------
    queryset = Product.objects.all()
    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields=['collection_id','unit_price']
    search_fields =['name']
    ordering_fields =["buying_price"]
    filterset_class= ProductFilter

    pagination_class = DeafualtPagination

    serializer_class= ProductSerializer

   
    def get_serializer_context(self):
        return {'request':self.request}




class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class= CollectionSerializer
    def get_serializer_context(self):
        return {'request':self.request}

class ReviewViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
    serializer_class= ReviewSerializer
    def get_serializer_context(self):
        print(self.kwargs['product_pk'],'^'*10)
        return {'product_id':self.kwargs['product_pk']}