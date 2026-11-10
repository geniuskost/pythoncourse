from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='contacts'),
    re_path(r'^(?P<country>[\w-]+)/?$', views.office, name='office'),
    re_path(r'^.+$', RedirectView.as_view(pattern_name='contacts')),
]
