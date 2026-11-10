from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts'),
    re_path(r'^(?P<country>[\w-]+)/?$', views.OfficeView.as_view(), name='office'),
    re_path(r'^.+$', RedirectView.as_view(pattern_name='contacts')),
]
