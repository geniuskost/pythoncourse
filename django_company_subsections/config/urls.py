from django.contrib import admin
from django.urls import include, path, re_path

from company.views import PageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PageView.as_view(key='home'), name='home'),
    re_path(r'^news(?:/.*)?$', PageView.as_view(key='news'), name='news'),
    re_path(r'^management(?:/.*)?$', PageView.as_view(key='management'), name='management'),
    re_path(r'^about(?:/.*)?$', PageView.as_view(key='about'), name='about'),
    re_path(r'^contacts?(?:/|$)', include('offices.urls')),
]

handler404 = 'company.views.not_found'
