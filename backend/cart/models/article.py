from django.db import models


class Article(models.Model):
    
    name = models.CharField('name', max_length=32)
    price = models.DecimalField('price', max_digits=6, decimal_places=2)
    model = models.CharField('model', max_length=32, null=True, blank=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
