
from django.db import models
from uuid import uuid4
from mosh.models import Product,Collection
 

# Create your models here.



class Cart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    productname = models.CharField(max_length=100, null=True)
    created_at= models.DateField(auto_now_add=True)
    class Meta:
        permissions=[
            ('cancel_order','Can cancel Order')
        ]



class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True,related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price =models.IntegerField()

    class meta:
        unique_together=[['cart','product']]

class OrderItem(models.Model):
    order = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True,related_name="order")
    # cart = models.ForeignKey(CartItems, on_delete=models.CASCADE, null=True,related_name="cartitem")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price =models.IntegerField( null=True)

        