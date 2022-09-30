
from django.urls import path,include
from . import views

urlpatterns = [ 
    path('', views.master, name='master'),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path("login/", views.MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("profile/", views.ProfileView.as_view(), name="profile"),



]