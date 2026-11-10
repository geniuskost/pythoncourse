from django.shortcuts import redirect, render
from django.views.generic import TemplateView

NEWS = [
    {
        'date': '28.10.2026',
        'title': 'Новий офіс в Одесі',
        'text': 'Ми переїхали в сучасний простір у центрі міста: більше світла, більше місця для команди.',
        'image': 'company/img/news-1.svg',
    },
    {
        'date': '15.10.2026',
        'title': 'Запуск оновленого сайту',
        'text': 'Новий сайт з розділами про компанію, керівництво та офіси в різних країнах.',
        'image': 'company/img/news-2.svg',
    },
    {
        'date': '02.10.2026',
        'title': 'Команда зросла до 120 людей',
        'text': 'До нас приєдналися нові розробники, дизайнери та аналітики з трьох країн.',
        'image': 'company/img/news-3.svg',
    },
    {
        'date': '20.09.2026',
        'title': 'Партнерство з європейським ринком',
        'text': 'Відкрито представництва у Франції та Австрії для роботи з клієнтами в ЄС.',
        'image': 'company/img/news-1.svg',
    },
]

MANAGEMENT = [
    {'name': 'Олена Коваленко', 'role': 'Генеральний директор', 'initials': 'ОК',
     'bio': 'Очолює компанію з 2015 року. Відповідає за стратегію та розвиток.'},
    {'name': 'Андрій Мельник', 'role': 'Технічний директор', 'initials': 'АМ',
     'bio': 'Керує розробкою та архітектурою всіх продуктів компанії.'},
    {'name': 'Ірина Шевченко', 'role': 'Фінансовий директор', 'initials': 'ІШ',
     'bio': 'Відповідає за бюджет, звітність і міжнародні розрахунки.'},
    {'name': 'Максим Бондаренко', 'role': 'Директор з розвитку', 'initials': 'МБ',
     'bio': 'Будує партнерства та відкриває нові ринки.'},
]

TIMELINE = [
    ('2010', 'Заснування компанії в Одесі, команда з п’яти людей.'),
    ('2014', 'Перший великий проєкт для міжнародного замовника.'),
    ('2018', 'Команда виросла до 50 співробітників, з’явився другий офіс.'),
    ('2022', 'Запуск власного продукту та перехід на віддалену роботу.'),
    ('2026', 'Представництва у Франції та Австрії, 120 співробітників.'),
]

STATS = [('16', 'років на ринку'), ('120', 'співробітників'), ('3', 'країни'), ('250+', 'проєктів')]


class HomeView(TemplateView):
    template_name = 'company/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = NEWS[:3]
        return context


class NewsView(TemplateView):
    template_name = 'company/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NEWS
        return context


class ManagementView(TemplateView):
    template_name = 'company/management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = MANAGEMENT
        return context


class AboutView(TemplateView):
    template_name = 'company/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = STATS
        return context


class HistoryView(TemplateView):
    template_name = 'company/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = TIMELINE
        return context


def section_redirect(request, section):
    return redirect(section)


def not_found(request, exception=None):
    return render(request, '404.html', status=404)
