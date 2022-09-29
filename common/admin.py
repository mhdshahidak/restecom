from django.contrib import admin
from . models import Product,Collection,User

# Register your models here.

# admin.site.register(ProductCatogory)
admin.site.register(Product)
# admin.site.register(ProductImage)
admin.site.register(Collection)
admin.site.register(User)