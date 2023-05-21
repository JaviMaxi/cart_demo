from rest_framework import serializers
from cart.models import CartItem
from cart.serializers.article import ArticleSerializer

class CartItemSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = (
            'id', 
            'article',
            'quantity',
        )
        