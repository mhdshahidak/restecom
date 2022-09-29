from typing import Collection
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class ProductCatogory(models.Model):
#     catagory_name = models.CharField(max_length=40)

class Collection(models.Model):
    category = models.CharField(max_length=100, null = True)

class Product(models.Model):
    name = models.CharField(max_length=100, null = True)
    buying_price = models.FloatField( null = True)
    max_offer_price = models.FloatField( null = True)
    qty = models.IntegerField( null = True)
    collection = models.ForeignKey(Collection,on_delete = models.CASCADE,null=True)
    
   


class User(AbstractUser):
    @property
    def fullname(self):
        if self.first_name and self.last_name:
            return str(f"{self.first_name} {self.last_name}")
        elif self.first_name:
            return str(f"{self.first_name}")
        else:
            return self.username