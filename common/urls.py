from . import views
from django.urls import path,include

urlpatterns = [ 
    path('', views.master, name='master'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('collection/<int:pk>/', views.collection_detail, name='collection-detail'),
    path('work', views.work, name='work'),
    path("register/", views.RegisterView.as_view(), name="auth_register"),


]