from . import views
from django.urls import path,include

urlpatterns = [ 
    path('', views.master, name='master'),
    path('detail/<int:id>/', views.detail, name='detail'),
]