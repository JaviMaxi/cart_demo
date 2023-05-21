from django.db import models


class Category(models.Model):

    name = models.CharField('name', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
