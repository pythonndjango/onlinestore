from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Manufacturer(models.Model):
        name = models.CharField(max_length=50)
        city = models.CharField(max_length=100)
        active = models.BooleanField(default=True)

        def __str__(self):
            return self.name


class Product(models.Model):
    
    manufacturer = models.ForeignKey(Manufacturer,
                                    on_delete=models.CASCADE,
                                    related_name="products")
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField()
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name