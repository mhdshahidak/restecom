
from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers

from . import views



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


