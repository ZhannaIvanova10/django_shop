from django.shortcuts import render
from .models import Product


def home(request):
    """Контроллер для главной страницы"""
    # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    
    # Выводим в консоль для дополнительного задания
    print("=" * 50)
    print("Последние 5 добавленных продуктов:")
    for i, product in enumerate(latest_products, 1):
        print(f"{i}. {product.name} - {product.price} руб. ({product.category.name})")
    print("=" * 50)
    
    context = {
        'title': 'Главная страница',
        'message': 'Добро пожаловать в наш интернет-магазин!',
        'latest_products': latest_products,
    }
    return render(request, 'catalog/home.html', context)
def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        print(f"Новое сообщение от {name} ({phone}): {message}")
        
        context = {
            'title': 'Контакты',
            'message': 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.',
            'success': True,
        }
        return render(request, 'catalog/contacts.html', context)
    
    context = {
        'title': 'Контакты',
        'message': 'Свяжитесь с нами',
        'success': False,
    }
    return render(request, 'catalog/contacts.html', context)
