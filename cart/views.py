from django.shortcuts import render,redirect
from users.models import UserProfile
from items.models import Item
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/users/user_login/")
def view_cart(request):
    current_user_name = request.user.username
    user = User.objects.filter(username=current_user_name).first()
    user_loggedin = UserProfile.objects.filter(user = user).first()
    items = user_loggedin.cart.cart_item.all()
    total = 0
    for item in items:
        total += (item.item_price*(1 - (item.item_discount)/100))

    return render(request, 'cart/cart.html', {'items':items, 'cart_total':total})


@login_required(login_url="/users/user_login/")
def remove_item(request, item_id):
    current_user_name = request.user.username
    user = User.objects.filter(username=current_user_name).first()
    user_loggedin = UserProfile.objects.filter(user=user).first()
    item = user_loggedin.cart.cart_item.get(pk=item_id)
    user_loggedin.cart.cart_item.remove(item)
    items = user_loggedin.cart.cart_item.all()
    return render(request, 'cart/cart.html', {'items':items})


@login_required(login_url="/users/user_login/")
def add_item(request, item_id):
    item_id = int(item_id)
    current_user_name = request.user.username
    user = User.objects.filter(username=current_user_name).first()
    user_loggedin = UserProfile.objects.filter(user=user).first()
    item = Item.objects.get(pk=item_id)
    user_loggedin.cart.cart_item.add(item)
    items = user_loggedin.cart.cart_item.all()
    return redirect('cart:view_cart')


@login_required(login_url="/users/user_login/")
def check_out(request):
    current_user_name = request.user.username
    user = User.objects.filter(username=current_user_name).first()
    user_loggedin = UserProfile.objects.filter(user=user).first()
    items = user_loggedin.cart.cart_item.all()
    print(items)
    print(type(items))
    for item in items:
        user_loggedin.cart.cart_item.remove(item)
    return render(request, 'cart/payment.html')


@login_required(login_url="/users/user_login/")
def payments(request):
    return render(request, 'cart/order_success.html')