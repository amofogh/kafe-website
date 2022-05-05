from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class ItemCategories(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class MenuItems(models.Model):
    name = models.CharField(max_length=100, verbose_name='item name')
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='items/')
    type = models.ForeignKey(ItemCategories, on_delete=models.CASCADE, verbose_name='Item type')
    active = models.BooleanField(default=True, verbose_name='activate item')
    show_menu = models.BooleanField(default=False, verbose_name='show in menu tab')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return self.name


# class SpecialOffers(models.Model):
#     food = models.ForeignKey('MenuItems', on_delete=models.CASCADE, verbose_name='food for special offer')
#
