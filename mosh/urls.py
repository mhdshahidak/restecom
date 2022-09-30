from . import views
from django.urls import path,include

urlpatterns = [ 
    path('', views.master, name='master'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('collection/<int:pk>/', views.collection_detail, name='collection-detail'),
    path('Productlist', views.Productlist.as_view()),
    path('Productlistgeneric', views.Productlistgeneric.as_view()),
    path('ProductDeatils/<int:pk>/', views.ProductDeatils.as_view()),
    

    
    

]