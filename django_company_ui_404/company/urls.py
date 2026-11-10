from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('management/', views.ManagementView.as_view(), name='management'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/history/', views.HistoryView.as_view(), name='history'),
    re_path(r'^about/history$', RedirectView.as_view(pattern_name='history')),
    re_path(r'^(?P<section>news|management|about)(?:/.+)?$', views.section_redirect),
    re_path(r'^contacts$', RedirectView.as_view(pattern_name='contacts')),
    re_path(r'^(?:home|index|main)/?$', RedirectView.as_view(pattern_name='home')),
    re_path(r'^(?:team|company)/?$', RedirectView.as_view(pattern_name='about')),
]
