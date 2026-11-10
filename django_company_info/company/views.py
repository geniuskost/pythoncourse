from django.shortcuts import render

NAV = [
    ('home', '/', 'Головна'),
    ('news', '/news/', 'Новини'),
    ('management', '/management/', 'Керівництво'),
    ('about', '/about/', 'Про компанію'),
    ('contacts', '/contacts/', 'Контакти'),
]

PAGES = {
    'home': {
        'title': 'Моя компанія',
        'lead': 'Ласкаво просимо на сайт компанії «Моя компанія».',
        'items': [],
    },
    'news': {
        'title': 'Новини',
        'lead': 'Останні події компанії.',
        'items': [
            'Компанія відкрила новий офіс в Одесі.',
            'Запущено оновлену версію сайту.',
            'Команда зросла до 120 співробітників.',
        ],
    },
    'management': {
        'title': 'Керівництво компанії',
        'lead': 'Люди, які ведуть компанію вперед.',
        'items': [
            'Олена Коваленко — генеральний директор',
            'Андрій Мельник — технічний директор',
            'Ірина Шевченко — фінансовий директор',
        ],
    },
    'about': {
        'title': 'Про компанію',
        'lead': 'Ми працюємо з 2010 року та створюємо програмні продукти для бізнесу.',
        'items': [],
    },
    'contacts': {
        'title': 'Контакти',
        'lead': 'Зв’яжіться з нами будь-яким зручним способом.',
        'items': [
            'Адреса: м. Одеса, вул. Дерибасівська, 1',
            'Телефон: +380 48 000 00 00',
            'Email: info@mycompany.example',
        ],
    },
}


def render_page(request, key):
    context = {'nav': NAV, 'current': key, 'page': PAGES[key]}
    return render(request, 'company/page.html', context)


def home(request):
    return render_page(request, 'home')


def news(request, *args):
    return render_page(request, 'news')


def management(request, *args):
    return render_page(request, 'management')


def about(request, *args):
    return render_page(request, 'about')


def contacts(request, *args):
    return render_page(request, 'contacts')


def not_found(request, exception=None):
    return render(request, '404.html', {'nav': NAV, 'current': None}, status=404)
