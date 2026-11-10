from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<country>france|ukraine|austria)/?$', views.OfficeView.as_view(), name='office'),
    re_path(r'^.*$', views.ContactsView.as_view(), name='contacts'),
]
