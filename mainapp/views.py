import datetime
import json
import os.path

from django.shortcuts import render, get_object_or_404

from basket.models import Basket
from mainapp.models import Product, ProductCategory

module_dir = os.path.dirname(__file__)

site_menu = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products:product', 'name': 'product'},
    {'href': 'contact', 'name': 'contact'},
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
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'all'}
        else:
            products = Product.objects.filter(category__pk=pk).order_by('price')
            category = get_object_or_404(ProductCategory, pk=pk)

        content = {
            "title": title,
            'site_menu': site_menu,
            "category_menu": categories,
            "category": category,
            "products": products,
            "basket": basket
        }

        return render(request, 'mainapp/products_list.html', content)

    products = Product.objects.all()

    content = {
        "title": title,
        'site_menu': site_menu,
        "category_menu": categories,
        "products": products[0:3],
        "basket": basket,
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
