import random
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Term
from .forms import TermForm

def home(request):
    """Отображает главную страницу приложения с приветствием.
    
    Args:
        request (HttpRequest): Объект запроса Django.
    
    Returns:
        HttpResponse: Рендер шаблона home.html.
    """
    return render(request, 'terms/home.html')

def terms_list(request):
    """Отображает список всех терминов в виде таблицы.
    
    Args:
        request (HttpRequest): Объект запроса Django.
    
    Returns:
        HttpResponse: Рендер шаблона terms_list.html
    """
    terms = Term.objects.all()
    return render(request, 'terms/terms_list.html', {'terms': terms})

def add_term(request):
    """Обрабатывает добавление нового термина через форму.
    
    Args:
        request (HttpRequest): Объект запроса Django.
    
    Returns:
        HttpResponseRedirect: Перенаправление на terms_list при успешном сохранении.
        HttpResponse: Рендер формы add_term.html с ошибками при невалидных данных.
    """
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Термин успешно добавлен!')
            return redirect('terms_list')
    else:
        form = TermForm()
    return render(request, 'terms/add_term.html', {'form': form})

def trainer(request):
    """Обрабатывает логику тренажёра терминов:
    - Показывает случайный термин (GET-запрос)
    - Проверяет ответ пользователя (POST-запрос)
    
    Args:
        request (HttpRequest): Объект запроса Django.
    
    Returns:
        HttpResponse: Варианты:
            - trainer.html (с случайным термином)
            - trainer_result.html (с результатом проверки)
            - redirect на home (если нет терминов в БД)
    """
    if request.method == 'POST':
        term_id = request.POST.get('term_id')
        user_answer = request.POST.get('latin', '').strip()
        term = Term.objects.get(id=term_id)
        is_correct = (user_answer.lower() == term.latin.lower())
        return render(request, 'terms/trainer_result.html', {
            'term': term,
            'is_correct': is_correct,
            'user_answer': user_answer
        })
    
    terms = Term.objects.all()
    if not terms:
        return redirect('home')
    random_term = random.choice(terms)
    return render(request, 'terms/trainer.html', {'term': random_term})

def stats(request):
    """Отображает статистику по терминам:
    - Общее количество терминов
    - Последний добавленный термин
    
    Args:
        request (HttpRequest): Объект запроса Django.
    
    Returns:
        HttpResponse: Рендер шаблона stats.html
    """
    total_terms = Term.objects.count()
    latest_term = Term.objects.last()
    return render(request, 'terms/stats.html', {
        'total_terms': total_terms,
        'latest_term': latest_term,
    })
