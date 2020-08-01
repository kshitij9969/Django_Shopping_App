from django.urls import path
from items import views


app_name = 'items'

urlpatterns = [
    path('search_item/', views.search_item , name='search_item'),
    path('view_item_details/<item_id>', views.view_item_details, name='view_item_details'),
]

