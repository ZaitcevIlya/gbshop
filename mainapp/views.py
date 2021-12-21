import datetime
import json
import os.path
import random

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from basket.models import Basket
from mainapp.models import Product, ProductCategory

module_dir = os.path.dirname(__file__)

site_menu = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products:product', 'name': 'products'},
    {'href': 'contact', 'name': 'contact'},
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_similar_products(hot_product):
    similar_products =Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return similar_products


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


def products(request, pk=None, page=1):
    # page = request.GET['page']
    title = 'Main'
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            category = {'name': 'all'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True).order_by('price')

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            "title": title,
            'site_menu': site_menu,
            "category_menu": categories,
            "category": category,
            "products": products_paginator,
            "basket": basket
        }

        return render(request, 'mainapp/products_list.html', content)


    hot_product = get_hot_product()
    similar_products = get_similar_products(hot_product)

    content = {
        "title": title,
        'site_menu': site_menu,
        "category_menu": categories,
        "hot_product": hot_product,
        "similar_products": similar_products,
        "basket": basket,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'Product'
    categories = ProductCategory.objects.all()

    content = {
        title: title,
        "category_menu": categories,
        "product": get_object_or_404(Product, pk=pk),
        "basket": get_basket(request.user),
        'site_menu': site_menu,
    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    context = {
        'site_menu': site_menu,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'mainapp/contact.html', context)
