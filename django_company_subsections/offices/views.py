from django.shortcuts import render

from company.views import NAV, PAGES

OFFICES = {
    'france': {
        'title': 'Офіс у Франції',
        'lead': 'Наш європейський хаб у Парижі.',
        'items': [
            'Адреса: Paris, 12 Rue de Rivoli',
            'Телефон: +33 1 00 00 00 00',
            'Email: france@mycompany.example',
        ],
    },
    'ukraine': {
        'title': 'Офіс в Україні',
        'lead': 'Головний офіс компанії в Одесі.',
        'items': [
            'Адреса: м. Одеса, вул. Дерибасівська, 1',
            'Телефон: +380 48 000 00 00',
            'Email: ukraine@mycompany.example',
        ],
    },
    'austria': {
        'title': 'Офіс в Австрії',
        'lead': 'Представництво у Відні.',
        'items': [
            'Адреса: Wien, Kärntner Straße 5',
            'Телефон: +43 1 000 00 00',
            'Email: austria@mycompany.example',
        ],
    },
}


def index(request, *args):
    page = dict(PAGES['contacts'])
    page['items'] = [
        'Офіс у Франції: /contacts/france',
        'Офіс в Україні: /contacts/ukraine',
        'Офіс в Австрії: /contacts/austria',
    ]
    context = {'nav': NAV, 'current': 'contacts', 'page': page}
    return render(request, 'company/page.html', context)


def office(request, country):
    context = {'nav': NAV, 'current': 'contacts', 'page': OFFICES[country]}
    return render(request, 'company/page.html', context)
