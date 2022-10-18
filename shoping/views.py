
from django.shortcuts import render



from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny,DjangoModelPermissions,IsAdminUser

from .models import Cart,CartItems
from mosh.models import Employee
from .serializers import AddCartItemsListerializer, Cartserializer,CartItemserializer,CartItemsListerializer,UpdateCartItemsListerializer,EmployeeSerializer
from web.permission import FullDjangoModelPermission,ViewCustomerHistoryPermission
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
    


class EmployeeViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    queryset= Employee.objects.all()   
    serializer_class = EmployeeSerializer
    permission_classes=[IsAdminUser]
    def get_permissions(self):
        if self.request.method ==" GET":
            return[AllowAny()]
        return[IsAuthenticated()]  
    @action(detail=False,methods=['GET','PUT'])
    def me(self,request):
        (employee,created) = Employee.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer=EmployeeSerializer(employee)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer=EmployeeSerializer(employee,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @action(detail=True,permission_classes=[ViewCustomerHistoryPermission])        
    def history(self,request,pk):
        return Response('ok')






