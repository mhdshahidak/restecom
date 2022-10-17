from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers

from . import views


router = DefaultRouter()
router.register('cart',views.CartViewset)
router.register('item',views.CartViewset)
router.register('employee',views.EmployeeViewSet)
# urlpatterns=router.urls

carts_router=routers.NestedDefaultRouter(router,'cart',lookup='cart')
carts_router.register('item',views.CartItemViewset, basename="cart-item")
urlpatterns=router.urls +carts_router.urls