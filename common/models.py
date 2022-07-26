from django.db import models

# Create your models here.

class ProductCatogory(models.Model):
    catagory_name = models.CharField(max_length=40)

class ProductImage(models.Model):
    image = models.ImageField(upload_to = 'product')

class Product(models.Model):
    name = models.CharField(max_length=100)
    catagory = models.ForeignKey(ProductCatogory, on_delete=models.CASCADE)
    procut_image = models.ManyToManyField(ProductImage)
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    max_offer_price = models.FloatField()
    qty = models.IntegerField()

