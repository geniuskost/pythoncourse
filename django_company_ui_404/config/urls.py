from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from company import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
    path('contacts/', include('offices.urls')),
    re_path(r'^contact(?:/.*)?$', RedirectView.as_view(pattern_name='contacts')),
    re_path(r'^.*$', views.not_found),
]

handler404 = 'company.views.not_found'
