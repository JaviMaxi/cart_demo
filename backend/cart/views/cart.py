from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from cart.serializers import CartSerializer



class CartList(generics.ListCreateAPIView):
    """
    View to list and create carts.
    """
    
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """
        Get the queryset of carts.

        Returns:
            - queryset: The queryset of carts.

        Query Parameters:
            - cart_id: (Optional) Filter the queryset by cart ID.
        """
        
        queryset = super().get_queryset()
        cart_id = self.request.GET.get('cart_id')

        if cart_id:
            queryset = queryset.filter(id=cart_id)

        return queryset

    def list(self, request, *args, **kwargs):
        """
        List carts.

        Returns:
            - HTTP 200 OK: If the carts are retrieved successfully.
        """
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    