from django.urls import path
from cart import views

app_name = 'cart'


urlpatterns = [
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove/<item_id>', views.remove_item, name='remove_item'),
    path('add_item/<item_id>', views.add_item, name='add_item'),
    path('check_out/', views.check_out, name='check_out'),
    path('payments/', views.payments, name='payments'),
]