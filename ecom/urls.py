from . import views
from django.urls import path,include

urlpatterns = [ 
    path('',views.index, name='index'),
    # path('edit/<int:id>',views.editdrink_list,name='editdrink_list'),
]
