import datetime
import json
import os.path

from django.shortcuts import render

module_dir = os.path.dirname(__file__)

site_menu = [
    {'href': 'index', 'name': 'home'},
    {'href': 'products', 'name': 'products'},
    {'href': 'contact', 'name': 'contact'},
]

links_menu = [
    {'href': 'products_all', 'name': 'all'},
    {'href': 'products_home', 'name': 'home'},
    {'href': 'products_office', 'name': 'office'},
    {'href': 'products_classic', 'name': 'classic'},
]


def base(request):
    context = {
        'name': 'my',
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/base.html', context)


def index(request):
    context = {
        'title': 'GB Shop',
        'site_menu': site_menu,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    with open(file_path) as f:
        products = json.load(f)

    context = {
        'products': products,
        'links_menu': links_menu,
        'site_menu': site_menu,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'site_menu': site_menu,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/contact.html', context)


