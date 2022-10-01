from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("", views.master, name="master"),
    path("login", views.login, name="login"),
    path("demo", views.demo, name="demo"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("collection/<int:pk>/", views.collection_detail, name="collection-detail"),
    path("Productlist", views.Productlist.as_view()),
    path("Productlistgeneric", views.Productlistgeneric.as_view()),
    path("ProductDeatils/<int:pk>/", views.ProductDeatils.as_view()),
    path('check-user/',views.CheckUser.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout',views.Logout.as_view()),
    path('user-details/',views.UserDetails.as_view()),

]
