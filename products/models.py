from django.db import models
from user.models import MyUser
# Create your models here.


class Category(models.Model):
    slug_categoty = models.CharField(max_length=500)
    name_category = models.CharField(max_length=500)
    image_category = models.ImageField(default="")

    def __str__(self):
        return self.name_category


class Products(models.Model):
    slug_product = models.CharField(max_length=500)
    name_product = models.CharField(max_length=500)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="Who_created")
    describe = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    main_picture = models.ImageField(default="")
    category = models.ManyToManyField(Category, related_name="CategoryOfProduct")
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    num_available = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_product


class ProductPictures(models.Model):
    image_product = models.ImageField()
    product = models.ForeignKey(Products,on_delete=models.CASCADE, related_name="PictureOfProduct")

    def __str__(self):
        return self.product
