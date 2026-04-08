from django.shortcuts import render

def home(request):
    """Главная страница (каталог)"""
    return render(request, 'catalog/home.html')

def contacts(request):
    """Страница контактов с обработкой формы"""
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Печатаем в консоль (можно заменить на отправку email или сохранение в БД)
        print(f"Получено сообщение от {name} ({email}): {message}")
        # Передаём контекст для показа сообщения об успехе
        return render(request, 'catalog/contacts.html', {'success': True})
    return render(request, 'catalog/contacts.html')
