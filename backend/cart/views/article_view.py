from rest_framework import generics
from cart.models import Article
from cart.serializers import ArticleSerializer
from rest_framework.permissions import AllowAny


class ArticleList(generics.ListCreateAPIView):
    """
    View to list and create articles.
    """
    
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Get the queryset of articles based on the provided filters.

        Returns:
            - queryset (QuerySet): Filtered and sorted queryset of articles.
        """
        
        queryset = super().get_queryset()

        price_filter = self.request.GET.getlist('price_filter[]')
        order_filter = self.request.GET.get('order_filter')
        category_filter = self.request.GET.get('category_filter')

        if price_filter:
            min_value = price_filter[0]
            max_value = price_filter[1]
            queryset = queryset.filter(price__gte=min_value, price__lte=max_value)
        if order_filter:
            queryset = queryset.order_by(order_filter)
        if category_filter:
            queryset = queryset.filter(category_id=category_filter)

        return queryset 