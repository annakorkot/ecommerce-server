from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    category= models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.productname