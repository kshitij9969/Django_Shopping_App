from django.shortcuts import render
from django.db.models import Q
from items.models import Item
from users.models import UserProfile
from django.contrib.auth.admin import User
from django.http import HttpResponseRedirect
from items.forms import SearchQueryForm
# Create your views here.


def in_cart_check(item_id, cart_items):
    for cart_item in cart_items:
        if cart_item.id == item_id:
            return True

    return False


def search_item(request):
    query = request.GET['query']
    current_user_name = request.user.username
    user = User.objects.filter(username=current_user_name).first()
    user_loggedin = UserProfile.objects.filter(user=user).first()
    if user_loggedin is not None:
        if request.method == 'GET':
            if query is None:
                print('inside get')
                query = request.GET['query']
                lookups = Q(item_name__startswith=query) | Q(item_description__startswith=query)
                results = Item.objects.filter(lookups).distinct()
                item_status = {}
                current_user_name = request.user.username
                user = User.objects.filter(username=current_user_name).first()
                user_loggedin = UserProfile.objects.filter(user=user).first()
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
                return render(request, 'core/index.html', {'results': results, 'final_item_status':final_item_status})
            if query is not None:
                lookups = Q(item_name__startswith=query)|Q(item_description__startswith=query)
                results = Item.objects.filter(lookups).distinct()
                item_status = {}
                current_user_name = request.user.username
                user = User.objects.filter(username=current_user_name).first()
                user_loggedin = UserProfile.objects.filter(user=user).first()
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

                return render(request, 'core/index.html', {'results': results, 'final_item_status':final_item_status})
    else:
        if query is None:
            results = Item.objects.all()
            final_item_status = []
            return render(request, 'core/index.html', {'results': results, 'final_item_status': final_item_status})
        else:
            lookups = Q(item_name__startswith=query) | Q(item_description__startswith=query)
            results = Item.objects.filter(lookups).distinct()
            final_item_status = []
            return render(request, 'core/index.html', {'results': results, 'final_item_status': final_item_status})


def view_item_details(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'items/product_details.html', {'item': item})
