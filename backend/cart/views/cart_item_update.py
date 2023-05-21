from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from cart.models import CartItem
from cart.models import Cart

class CartItemUpdateView(APIView):
    """
    View to update the quantity of a cart item.
    """
    
    
    queryset = CartItem.objects.all()
    permission_classes = [AllowAny]

    def patch(self, request):
        """
        Update the quantity of a cart item with the provided article ID.

        Returns:
            - HTTP 200 OK: If the cart item is updated successfully.
            - HTTP 404 Not Found: If the cart item does not exist in the cart.

        Raises:
            - Article.DoesNotExist: If the provided article ID does not exist.
        """
        
        article_id = request.data.get('article')
        quantity = request.data.get('quantity')
        cart = Cart.objects.first()
        cart_items = CartItem.objects.filter(article_id=article_id, cart=cart)
        if cart_items.count() > 0:
            cart_items.update(quantity=quantity)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)