from django.shortcuts import render



from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.response import Response

from .models import Cart,CartItems
from .serializers import Cartserializer,CartItemserializer,CartItemsListerializer
# Create your views here.

# only want yo create get and delect so we create a modelviewset
class CartViewset(CreateModelMixin,GenericViewSet,RetrieveModelMixin,DestroyModelMixin):
    queryset =Cart.objects.prefetch_related('items__product').all()
    # def retrive(self, request, pk):
    #     user = self.get_object(pk)
    #     print(user.query)
    #     user = Cartserializer(user)
    #     return Response(user.data)
    serializer_class = Cartserializer


class CartItemViewset(ModelViewSet,ListModelMixin):
    serializer_class = CartItemsListerializer
    def get_queryset(self):
        return CartItems.objects.filter(cart_id=self.kwargs['cart_pk'])
    