from django import template
from cart.models import Cart
from users.models import UserProfile

register = template.Library()


@register.simple_tag
def in_cart(item_id, user):
    user_in = UserProfile.objects.filter(user=user).first()
    if user_in.cart.cart_item.get(item_id):
        return True
    else:
        return False


@register.simple_tag
def final_price(price, discount):
    return price*(1-0.01*discount)