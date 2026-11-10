from django.shortcuts import redirect
from django.views.generic import TemplateView

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


class ContactsView(TemplateView):
    template_name = 'offices/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offices'] = OFFICES
        return context


class OfficeView(TemplateView):
    template_name = 'offices/office.html'

    def get(self, request, country, **kwargs):
        if country not in OFFICES:
            return redirect('contacts')
        return super().get(request, country=country, **kwargs)

    def get_context_data(self, country, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(office=OFFICES[country], slug=country)
        return context
