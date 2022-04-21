from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)