from django.db import models

class Cart(models.Model):
    country = models.CharField('Country', max_length=32, default="Spain")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        """
        Calculates the total value of the cart.

        Returns:
            - The total value of the cart, summing up the total value of each item in the cart.
        """
        
        total = 0
        for item in self.items.all():
            total += item.total
        return total

    def __str__(self):
        return f'{self.created_at}'

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        
