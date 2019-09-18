from django.urls import path, re_path
from django.views.decorators.cache import cache_page

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.category_ajax)),
    path('category/<int:pk>/', mainapp.category, name='category'),
    path('category/<int:pk>/<int:page>/', mainapp.category, name='category'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.category_ajax)),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('contacts/', mainapp.contacts, name='contacts'),
]
