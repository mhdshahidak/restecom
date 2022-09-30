

from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Collection, Product
from .serializers import ProductSerializer,CollectionSerializer,ExeSerializer
from rest_framework import status 
from django.db.models import Count
from . import serializers


from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.


@api_view(['GET','POST'])
def master(request):
    if request.method =='GET':
        proall=Product.objects.select_related('collection').all()
        serializer=ProductSerializer(proall,many=True,context={
            'request':request
        })
        return Response(serializer.data)
    elif request.method =='POST':  

        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','PATCH','DELETE'])
def detail(request,id):
    # 1st method


    # --------------------------------------------------------
    # try:
    #     productobj=Product.objects.get(id=id)
    #     serializer=ProductSerializer(productobj)
        
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)   
     # --------------------------------------------------------    


    # 2nd method to avoid Continous try and except
    productobj=get_object_or_404(Product ,pk=id)
    if request.method =='GET':
        serializer=ProductSerializer(productobj)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=ProductSerializer(productobj,data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    elif request.method =='DELETE':  
        # condition where we cannot delect it
        # if productobj.price_set.count()>0:
        #     return Response({'error':"item cant be delected"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        # else:
            
        productobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view()
def collection_detail(request , pk):
    # productobj=get_object_or_404(Collection ,instance=pk)
    productobj=Collection.objects.get(id=pk)
    serializer=CollectionSerializer(productobj)
        
    return Response(serializer.data)







# class based view 
class Productlist(APIView):
    def get(self,request):
        proall=Product.objects.select_related('collection').all()
        serializer=ProductSerializer(proall,many=True,context={
            'request':request
        })
        return Response(serializer.data)
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)




# generic view
class Productlistgeneric(ListCreateAPIView):

    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()
# or
    queryset =Product.objects.select_related('collection').all()
    # def get_serializer_class(self):
    #     return ProductSerializer
# or
    serializer_class= ProductSerializer
    def get_serializer_context(self):
        return {"request":self.request} 



# customizing generic view
# get update delete

class ProductDeatils(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    # costomize delect with another query
    # def delete(self, request, *args, **kwargs):
    #     return super().delete(request, *args, **kwargs)

    def get_serializer_context(self):
        return {"request":self.request} 

