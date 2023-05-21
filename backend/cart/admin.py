from django.contrib import admin
from .models import Article
from .models import Cart
from .models import CartItem
from .models import Category


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)