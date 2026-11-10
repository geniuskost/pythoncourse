from django.shortcuts import redirect, render

OFFICES = {
    'france': {
        'name': 'Франція',
        'city': 'Париж',
        'flag': 'company/img/flag-france.svg',
        'address': '12 Rue de Rivoli, 75001 Paris',
        'phone': '+33 1 00 00 00 00',
        'email': 'france@mycompany.example',
        'description': 'Наш європейський хаб: працюємо з клієнтами з Франції, Бельгії та Швейцарії.',
    },
    'ukraine': {
        'name': 'Україна',
        'city': 'Одеса',
        'flag': 'company/img/flag-ukraine.svg',
        'address': 'вул. Дерибасівська, 1, Одеса',
        'phone': '+380 48 000 00 00',
        'email': 'ukraine@mycompany.example',
        'description': 'Головний офіс компанії: розробка, дизайн і підтримка продуктів.',
    },
    'austria': {
        'name': 'Австрія',
        'city': 'Відень',
        'flag': 'company/img/flag-austria.svg',
        'address': 'Kärntner Straße 5, 1010 Wien',
        'phone': '+43 1 000 00 00',
        'email': 'austria@mycompany.example',
        'description': 'Представництво для роботи з ринками Центральної Європи.',
    },
}


def index(request):
    return render(request, 'offices/contacts.html', {'offices': OFFICES})


def office(request, country):
    data = OFFICES.get(country)
    if data is None:
        return redirect('contacts')
    return render(request, 'offices/office.html', {'office': data, 'slug': country})
