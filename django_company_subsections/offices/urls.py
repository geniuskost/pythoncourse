from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<country>france|ukraine|austria)/?$', views.office, name='office'),
    re_path(r'^.*$', views.index, name='contacts'),
]
