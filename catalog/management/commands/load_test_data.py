from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур, очищая существующие'

    def handle(self, *args, **options):
        self.stdout.write('Очистка существующих данных...')
        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write('Загрузка фикстур...')
        call_command('loaddata', 'catalog/fixtures/categories.json')
        call_command('loaddata', 'catalog/fixtures/products.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
