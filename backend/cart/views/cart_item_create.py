from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from cart.serializers.cart_item import CartItemSerializer
from cart.models import CartItem
from cart.models import Cart

class CartItemCreateView(APIView):
    """
    View to create a new cart item.
    """
    
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Create a new cart item with the provided article ID.

        Returns:
            - HTTP 201 Created: If the cart item is created successfully.
            - HTTP 200 OK: If the cart item already exists in the cart.

        Raises:
            - Article.DoesNotExist: If the provided article ID does not exist.
        """
        
        article_id = request.data.get('article')
        if Cart.objects.exists():
            cart = Cart.objects.first()
        else:
            cart = Cart.objects.create()
        cart_item, created = CartItem.objects.get_or_create(article_id=article_id, cart=cart)
        if created:
            return Response({}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_200_OK)