from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Sale(models.Model):
    detail = models.CharField(max_length=256)
    quanty = models.IntegerField()
    total = models.IntegerField()
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.detail
