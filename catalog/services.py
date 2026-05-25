from django.core.cache import cache
from .models import Product, Category

def get_products_by_category(category_id):
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)
    if products is None:
        try:
            category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=category, is_published=True)
            cache.set(cache_key, products, 300)  # кеш на 5 минут
        except Category.DoesNotExist:
            products = Product.objects.none()
    return products
