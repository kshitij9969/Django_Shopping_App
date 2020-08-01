from django.db import models
from items.models import Item
# Create your models here.


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    cart_item = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.cart_id}, {self.cart_item}"