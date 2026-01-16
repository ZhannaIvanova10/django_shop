from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command
from pathlib import Path
class Command(BaseCommand):
    help = 'Загружает тестовые данные для каталога'
    
    def handle(self, *args, **options):
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        self.stdout.write('Загрузка данных из фикстур...')
        
        # Пытаемся загрузить из фикстур
        categories_fixture = Path('catalog/fixtures/category_data.json')
        products_fixture = Path('catalog/fixtures/product_data.json')
        
        if categories_fixture.exists() and products_fixture.exists():
            try:
                call_command('loaddata', 'category_data.json')
                self.stdout.write(self.style.SUCCESS('Категории загружены'))
                call_command('loaddata', 'product_data.json')
                self.stdout.write(self.style.SUCCESS('Продукты загружены'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Ошибка при загрузке фикстур: {e}'))
                self.create_test_data()
        else:
            self.stdout.write('Фикстуры не найдены, создаем тестовые данные...')
            self.create_test_data()
        
        self.stdout.write(self.style.SUCCESS('Все данные успешно загружены!'))
        self.stdout.write(f'Категорий: {Category.objects.count()}')
        self.stdout.write(f'Продуктов: {Product.objects.count()}')
    
    def create_test_data(self):
        """Создает тестовые данные если нет фикстур"""
        categories = [
            {'name': 'Электроника', 'description': 'Техника и гаджеты'},
            {'name': 'Одежда', 'description': 'Мужская и женская одежда'},
            {'name': 'Книги', 'description': 'Художественная и учебная литература'},
            {'name': 'Дом и сад', 'description': 'Товары для дома'},
            {'name': 'Спорт', 'description': 'Спортивные товары'},
        ]
        for cat_data in categories:
            Category.objects.create(**cat_data)
        
        categories_objs = Category.objects.all()
        
        products = [
            {
                'name': 'Ноутбук Lenovo',
                'description': 'Идеальный для работы и учебы',
                'category': categories_objs[0],
                'price': 45999.99
            },
            {
                'name': 'Смартфон iPhone',
                'description': 'Последняя модель',
                'category': categories_objs[0],
                'price': 89999.99
            },
            {
                'name': 'Джинсы',
                'description': 'Классические синие джинсы',
                'category': categories_objs[1],
                'price': 3499.99
            },
            {
                'name': 'Книга "Python Cookbook"',
                'description': 'Рецепты программирования на Python',
                'category': categories_objs[2],
                'price': 2499.99
            },
            {
                'name': 'Набор посуды',
                'description': 'Кухонная посуда 12 предметов',
                'category': categories_objs[3],
                'price': 12999.99
            },
            {
                'name': 'Велосипед',
                'description': 'Горный велосипед 21 скорость',
                'category': categories_objs[4],
                'price': 25999.99
            },
        ]
        
        for prod_data in products:
            Product.objects.create(**prod_data)
        
        self.stdout.write(self.style.SUCCESS('Тестовые данные созданы'))
