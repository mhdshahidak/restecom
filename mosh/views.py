
from django.shortcuts import get_object_or_404,render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Collection, Product
from common.models import User
from .serializers import CollectionSerializer, ProductSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import BasicUserPermission


# Create your views here.


@api_view(["GET", "POST"])
def master(request):
    if request.method == "GET":
        proall = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(proall, many=True, context={"request": request})
        return Response(serializer.data)
    elif request.method == "POST":

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def login(request):
    return render(request,'login.html')

def demo(request):
    return render(request,'index.html')



@api_view(["GET", "PUT", "PATCH", "DELETE"])
def detail(request, id):
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
    productobj = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(productobj)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(productobj, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == "DELETE":
        # condition where we cannot delect it
        # if productobj.price_set.count()>0:
        #     return Response({'error':"item cant be delected"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        # else:

        productobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def collection_detail(request, pk):
    # productobj=get_object_or_404(Collection ,instance=pk)
    productobj = Collection.objects.get(id=pk)
    serializer = CollectionSerializer(productobj)

    return Response(serializer.data)


# class based view
class Productlist(APIView):
    def get(self, request):
        proall = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(proall, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# generic view
class Productlistgeneric(ListCreateAPIView):

    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()
    # or
    queryset = Product.objects.select_related("collection").all()
    # def get_serializer_class(self):
    #     return ProductSerializer
    # or
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {"request": self.request}


# customizing generic view
# get update delete


class ProductDeatils(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # costomize delect with another query
    # def delete(self, request, *args, **kwargs):
    #     return super().delete(request, *args, **kwargs)

    def get_serializer_context(self):
        return {"request": self.request}




class CheckUser(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        if self.request.user.is_superuser == False and self.request.user.is_active == True:
            print('200,1st')
            return Response({'id':self.request.user.id}, status=status.HTTP_200_OK)
        if self.request.user.is_superuser == True and self.request.user.is_active == True and self.request.user.user != None:
            print('200,2nd')
            return Response({'id':self.request.user.id}, status=status.HTTP_200_OK)
        else:
            print('200,3rd')
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    # print('logount')
    permission_classes = [BasicUserPermission,]
    # def get(self):
    #     obj=User.objects.filter(user=self.request.user)
    #     print(obj,'^'*10)
       

    def post(self, request):
        refresh_token = request.data["refresh_token"]
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            # print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        user = request.user.email
        print(user)
        
        # branchName = request.user.branch.name
        # userSplit = user.split('@')
        # data = userSplit[0]
        return Response({'user':user}, status=status.HTTP_200_OK)

    