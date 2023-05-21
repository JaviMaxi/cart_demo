from rest_framework import generics
from cart.models import CartItem
from cart.serializers import CartItemSerializer
from rest_framework.permissions import AllowAny


class CartItemList(generics.ListCreateAPIView):
    """
    View to list and create cart items
    """
    
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]