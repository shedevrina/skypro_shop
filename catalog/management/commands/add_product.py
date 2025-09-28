from  django.core.management.base import BaseCommand
from unicodedata import category

from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add product to the database'

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name_category='Аналитика', description_category='Анализ и проектирование')

        products = [
            {'name_product': 'IT аналитик', 'category':category, 'price_all': 150000.00},
            {'name_product': 'Бизнес-аналитик', 'category': category, 'price_all': 65000.00}

        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name_product}: {product.category.description_category}'))

            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name_product}: {product.category.description_category}'))
