from django.contrib import admin

from .models import Collection, Product,Employee,Items,Review

# Register your models here.
admin.site.register(Product)
# admin.site.register(ProductImage)
admin.site.register(Collection)
admin.site.register(Employee)
admin.site.register(Items)
admin.site.register(Review)

