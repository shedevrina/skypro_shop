from django.db import models
from unicodedata import decimal


# Create your models here.


class Category(models.Model):
    name_category = models.CharField(
        max_length=150, verbose_name="Категория"
    )
    description_category = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name_category"]


class Product(models.Model):
    name_product = models.CharField(
        max_length=150, verbose_name="Наименование", unique=True
    )
    description_product = models.TextField(null=True, blank=True)

    image = models.ImageField(
        upload_to="product", verbose_name="Фотография"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    price_all = models.DecimalField(
        help_text="Введите стоимость покупки", decimal_places=2, max_digits=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name_product"]
