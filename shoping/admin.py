from django.contrib import admin
from .models import CartItems,Cart,OrderItem
# Register your models here.



admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(OrderItem)

