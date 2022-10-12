from django.shortcuts import render



from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.response import Response

from .models import Cart,CartItems
from .serializers import AddCartItemsListerializer, Cartserializer,CartItemserializer,CartItemsListerializer,UpdateCartItemsListerializer
# Create your views here.

# only want yo create get and delect so we create a modelviewset
class CartViewset(CreateModelMixin,GenericViewSet,RetrieveModelMixin,DestroyModelMixin):
    queryset =Cart.objects.prefetch_related('items__product').all()
    serializer_class = Cartserializer


class CartItemViewset(ModelViewSet,ListModelMixin):
    http_method_names= ['post','get','patch','DELETE']
    # 1st method------------------------------------------------------------
    # serializer_class = CartItemsListerializer
    # 2nd method------------------------------------------------------------
    def get_serializer_class(self):
        if self.request.method=="POST":
            return AddCartItemsListerializer
        elif self.request.method=="PATCH":
            return UpdateCartItemsListerializer    
        return CartItemsListerializer    
# for geting id throgh url
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}
    def get_queryset(self):
        return CartItems.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')
    