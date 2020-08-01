from django.shortcuts import render
from items.models import Item
from cart.models import Cart
from users.models import UserProfile
from django.contrib.auth.admin import User
from django.db.models import Q
# Create your views here.


def in_cart_check(item_id, cart_items):
    for cart_item in cart_items:
        if cart_item.id == item_id:
            return True

    return False


def index(request):
    results = Item.objects.all()
    item_status = {}
    current_user_name = request.user.username
    user = User.objects.filter(username=current_user_name).first()
    user_loggedin = UserProfile.objects.filter(user=user).first()
    if user_loggedin is not None:
        cart_items = user_loggedin.cart.cart_item.all()
        for item in results:
            item_status[item.id] = False

        ids = item_status.keys()
        for id in ids:
            if in_cart_check(id, cart_items):
                item_status[id] = True

        final_item_status = []
        for id in ids:
            if item_status[id]:
                final_item_status.append(id)
        return render(request, 'core/index.html', {'results':results, 'final_item_status':final_item_status})

    return render(request, 'core/index.html', {'results':results, 'final_item_status':[]})