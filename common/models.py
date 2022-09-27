from django.db import models

# Create your models here.

# class ProductCatogory(models.Model):
#     catagory_name = models.CharField(max_length=40)

# class ProductImage(models.Model):
#     image = models.ImageField(upload_to = 'product')

class Product(models.Model):
    name = models.CharField(max_length=100, null = True)
    buying_price = models.FloatField( null = True)
    max_offer_price = models.FloatField( null = True)
    qty = models.IntegerField( null = True)
    
   

