from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.item_detail, name='item_detail'),

]