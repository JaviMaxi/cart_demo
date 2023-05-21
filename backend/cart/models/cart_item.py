from django.db import models
from cart.models import Cart
from cart.models import Article

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        """
        Calculates the total for this item in the cart.

        Returns:
            - The calculated total, rounded to 2 decimal places.
        """
        
        return round(self.quantity * self.article.price, 2)

    def __str__(self):
        return f'{self.article} - {self.quantity}'

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'
        
