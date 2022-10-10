from cgitb import lookup
from pprint import pprint
from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers

# router = DefaultRouter()
# router.register('Productlist',views.ProductViewSet)
# router.register('collection',views.CollectionViewSet)

# urlpatterns=router.urls








# nested router
router = DefaultRouter()
router.register('Productlist',views.ProductViewSet,basename="products")
router.register('collection',views.CollectionViewSet)
Productsrouter = routers.NestedDefaultRouter(router,'Productlist',lookup='product')
Productsrouter.register('review',views.ReviewViewSet, basename="product-review")
urlpatterns=router.urls +Productsrouter.urls









# urlpatterns = [
#     path("", views.master, name="master"),
#     path("login", views.login, name="login"),
#     path("demo", views.demo, name="demo"),
#     path("product", views.product, name="product"),
#     path("register", views.register, name="register"),
#     path("registeremployeee", views.registeremployeee, name="registeremployeee"),
    
#     path("detail/<int:id>/", views.detail, name="detail"),
#     path("collection/<int:pk>/", views.collection_detail, name="collection-detail"),
#     path("Productlist", views.Productlist.as_view()),
#     path("Productlistgeneric", views.Productlistgeneric.as_view()),
#     path("ProductDeatils/<int:pk>/", views.ProductDeatils.as_view()),
#     path('check-user/',views.CheckUser.as_view()),
#     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/logout',views.Logout.as_view()),
#     path('user-details/',views.UserDetails.as_view()),
#     path('add-user',views.CreateView.as_view()),
#     path('employeeregistration',views.EmployeeRegisterView.as_view()),
#     path('ItemAdd',views.ItemAddView.as_view()),
    
    
    


# ]
