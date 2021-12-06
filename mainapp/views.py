import datetime
import json
import os.path

from django.shortcuts import render
from mainapp.models import Product, ProductCategory

module_dir = os.path.dirname(__file__)

site_menu = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products:index', 'name': 'products'},
    {'href': 'contact', 'name': 'contact'},
]

categories = [
    {'href': 'products/home', 'name': 'home'},
    {'href': 'products/office', 'name': 'office'},
    {'href': 'products/classic', 'name': 'classic'},
]


def base(request):
    context = {
        'name': 'my',
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/base.html', context)


def main(request):
    context = {
        'title': 'GB Shop',
        'site_menu': site_menu,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/main.html', context)


def products(request, pk=None):
    title = 'Main'
    products = Product.objects.all()
    content = {
        "title": title,
        "products": products,
        'categories': categories,
        'site_menu': site_menu,
        'current_product': products.first(),
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    context = {
        'site_menu': site_menu,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/contact.html', context)
