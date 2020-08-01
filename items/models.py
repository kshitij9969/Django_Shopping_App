from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_description = models.CharField(max_length=30)
    item_price = models.IntegerField()
    item_discount = models.FloatField()
    item_availability = models.BooleanField(default=False)
    item_category = models.CharField(max_length=20)
    item_image = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"ID: {self.pk}" \
               f"Name: {self.item_name}" \
               f"Price: {self.item_price}" \
               f"Description: {self.item_description}."


