from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с правами can_unpublish_product и delete_product'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа создана'))

        content_type = ContentType.objects.get_for_model(Product)
        # Право can_unpublish_product
        perm_unpublish, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type
        )
        # Право delete_product (стандартное)
        perm_delete = Permission.objects.get(codename='delete_product', content_type=content_type)

        group.permissions.add(perm_unpublish, perm_delete)
        self.stdout.write(self.style.SUCCESS('Права добавлены в группу'))
