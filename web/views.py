

from urllib import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from web.permission import IsAdminOrReadOnly
from .filters import ProductFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from mosh.models import Collection, Employee, Product, Review
from .serializers import ReviewSerializer,OrdrtSerializer,CreateOrdrtSerializer,UpdateOrdrtSerializer
from mosh.serializers import ProductSerializer, CollectionSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .pagination import DeafualtPagination
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
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
    permission_classes=[IsAdminOrReadOnly]
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


# -----------------------------------        
class OrderViewSet(ModelViewSet):
    http_method_names=['get','patch','delete','head','options']
    queryset=Collection.objects.all()
    # permission_classes=[AllowAny]
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAdminUser()]
        return[IsAuthenticated()]    
    def create(self, request, *args, **kwargs):
        serializer = CreateOrdrtSerializer(
            data=request.data,
            context={'user_id':self.request.user.id}
            )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrdrtSerializer(order)
        return Response(serializer.data)



    # def get_serializer_context(self):
    #     return {'user_id':self.request.user.id}

    def get_serializer_class(self):
        if self.request.method =='POST':
            return CreateOrdrtSerializer

        elif self.request.method =='PATCH':
            return UpdateOrdrtSerializer
        return OrdrtSerializer

    
