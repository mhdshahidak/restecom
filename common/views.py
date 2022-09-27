from itertools import product
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status 
# Create your views here.


@api_view()
def master(request):
    proall=Product.objects.all()
    serializer=ProductSerializer(proall,many=True)
    return Response(serializer.data)


@api_view()
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
    serializer=ProductSerializer(productobj)
        
    return Response(serializer.data)



