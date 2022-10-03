from django.db import models


# Create your models here.
class Collection(models.Model):
    category = models.CharField(max_length=100, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    buying_price = models.FloatField(null=True)
    max_offer_price = models.FloatField(null=True)
    qty = models.IntegerField(null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

class Employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
