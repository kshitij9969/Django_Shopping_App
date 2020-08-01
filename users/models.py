from django.db import models
from django.contrib.auth.admin import User
from cart.models import Cart
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_contact = models.IntegerField(null=True)
    address = models.TextField(null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}, {self.cart}"



