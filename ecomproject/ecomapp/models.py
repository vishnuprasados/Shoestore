from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Categories(models.Model):

    categoryname=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.categoryname

class Products(models.Model):

    pdctname=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    Categories=models.ForeignKey(Categories, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="media/")

    def __str__(self):
        return self.pdctname

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    
    status=models.CharField(max_length=100,choices=options,default="in-cart")


class Placeorder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    # cart=models.ForeignKey(Carts,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    order_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("order_placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("delivered","delivered")
    )
    
    status=models.CharField(max_length=100,choices=options,default="order_placed")
