from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from cart.serializers.cart import CartItemSerializer
from cart.models import Article
from cart.models import Cart
from cart.models import CartItem

class CartCreateView(APIView):
    """
    View to create a new cart.
    """
    
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        """
        Create a new cart with the provided data.
        
        Required POST Parameters:
            - country: The country for the cart.
            - items: A list of item data.

        Returns:
            - cart_id (int): The ID of the created cart.

        Raises:
            - serializers.ValidationError: If the item data is invalid.
        """
        
        country = request.data.get('country')
        items_data = request.data.get('items')

        serializer = CartItemSerializer(data=items_data, many=True)
        serializer.is_valid(raise_exception=True)

        cart = Cart.objects.create(country=country)

        for item_data in items_data:
            article_data = item_data['article']
            article, created = Article.objects.get_or_create(**article_data)
            CartItem.objects.create(cart=cart, article=article)

        return Response({'cart_id': cart.id}, status=201)