from rest_framework import generics
from cart.models import Category
from cart.serializers import CategorySerializer
from rest_framework.permissions import AllowAny


class CategoryList(generics.ListCreateAPIView):
    """
    View to list and create categories.
    """
    
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]