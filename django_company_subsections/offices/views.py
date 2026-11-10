from django.views.generic import TemplateView

from company.views import NAV

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


class ContactsView(TemplateView):
    template_name = 'offices/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(nav=NAV, current='contacts', offices=OFFICES)
        return context


class OfficeView(TemplateView):
    template_name = 'offices/office.html'

    def get_context_data(self, country, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(nav=NAV, current='contacts', office=OFFICES[country])
        return context
