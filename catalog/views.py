from django.shortcuts import render

def home(request):
    """Контроллер для главной страницы"""
    context = {
        'title': 'Главная страница',
        'message': 'Добро пожаловать в наш интернет-магазин!',
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == 'POST':
        # Обработка POST-запроса
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # В реальном проекте здесь сохраняем в БД или отправляем email
        print(f"Новое сообщение от {name} ({phone}): {message}")
        
        context = {
            'title': 'Контакты',
            'message': 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.',
            'success': True,
        }
        return render(request, 'catalog/contacts.html', context)
    # GET-запрос - просто отображаем форму
    context = {
        'title': 'Контакты',
        'message': 'Свяжитесь с нами',
        'success': False,
    }
    return render(request, 'catalog/contacts.html', context)
