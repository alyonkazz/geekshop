import json
import datetime
import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory


def get_catalog_menu():
    return ProductCategory.objects.all()


def get_hot_product():
    return random.choice(Product.objects.all())


def get_same_products(hot_product):
    return hot_product.category.product_set.exclude(pk=hot_product.pk)


def index(request):
    date = datetime.datetime.now()
    context = {
        'page_title': 'магазин',
        'date': date,
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    hot_product = get_hot_product()

    context = {
        'page_title': 'каталог',
        'catalog_menu': get_catalog_menu,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
    }
    return render(request, 'mainapp/catalog.html', context)


def category(request, pk, page=1):
    pk = int(pk)

    if pk == 0:
        category = {
            'pk': 0,
            'name': 'все'
        }
        category_catalog = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        category_catalog = category.product_set.all()

    paginator = Paginator(category_catalog, 2)
    try:
        category_catalog = paginator.page(page)
    except PageNotAnInteger:
        category_catalog = paginator.page(1)
    except EmptyPage:
        category_catalog = paginator.page(paginator.num_pages)

    context = {
        'title': 'раздел каталога',
        'catalog_menu': get_catalog_menu(),
        'category': category,
        'category_catalog': category_catalog,
    }
    return render(request, 'mainapp/category_catalog.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': 'страница продукта',
        'catalog_menu': get_catalog_menu(),
        'category': product.category,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)


def contacts(request):
    # with open('geekshop/locations.json', 'r', encoding='utf-8', errors='ignore') as f:
    #     locations = json.load(f)

    # def load_from_json(file_name):
    #     with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', errors='ignore') as infile:
    #         return json.load(infile)

    context = {
        'page_title': 'контакты',
        # 'location': locations,
        "phone": "+7-(555)-555-5555",
        "email": "email@mail.ru",
        "address": "11"
    }
    return render(request, 'mainapp/contacts.html', context)
