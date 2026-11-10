from django.contrib import admin
from django.urls import include, path, re_path

from company import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    re_path(r'^news(?:/.*)?$', views.news, name='news'),
    re_path(r'^management(?:/.*)?$', views.management, name='management'),
    re_path(r'^about(?:/.*)?$', views.about, name='about'),
    re_path(r'^contacts?(?:/|$)', include('offices.urls')),
]

handler404 = 'company.views.not_found'
