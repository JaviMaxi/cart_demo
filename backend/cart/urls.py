from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cart import views

urlpatterns = [
    path("articles/", views.ArticleList.as_view(), name='articles'),
    path("cart/", views.CartList.as_view(), name='cart'),
    path('cart/create/', views.CartCreateView.as_view(), name='cart_create'),
    path("cart-item/", views.CartItemList.as_view(), name='cart_item'),
    path('cart-item/add', views.CartItemCreateView.as_view(), name='add_cart_item'),
    path('cart-item/delete', views.CartItemDeleteView.as_view(), name='delete_cart_item'),
    path('cart-item/update', views.CartItemUpdateView.as_view(), name='update_cart_item'),
    path("categories/", views.CategoryList.as_view(), name='categories'),
]

urlpatterns = format_suffix_patterns(urlpatterns)