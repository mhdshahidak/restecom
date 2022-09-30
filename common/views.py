
from django.shortcuts import render,get_object_or_404
from .models import User

from . import serializers


from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


def master(request):
    return render(request,'master.html')


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserTokenObtainPairSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer   



class ProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        return self.request.user    