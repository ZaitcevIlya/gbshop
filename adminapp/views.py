from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from users.models import User
from mainapp.models import Product, ProductCategory
from users.forms import UserRegistrationForm
from adminapp.forms import UserEditAdminForm, ProductCategoryEditForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'users admin panel'

    users_list = User.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        "title": title,
        "objects": users_list
    }

    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'user create'

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))

    else:
        user_form = UserRegistrationForm()

    content = {
        "title": title,
        "update_form": user_form
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'user update'

    update_user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        update_form = UserEditAdminForm(request.POST, request.FILES, instance=update_user)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[update_user.pk]))

    else:
        update_form = UserEditAdminForm(instance=update_user)

    content = {
        'title': title,
        'update_form': update_form
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'user update'

    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        "title": title,
        "user_to_delete": user
    }

    return render(request, 'adminapp/user_delete.html', content)




@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'categories admin panel'

    categories_list = ProductCategory.objects.all()

    content = {
        "title": title,
        "objects": categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'category create'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))

    else:
        category_form = ProductCategoryEditForm()

    content = {
        "title": title,
        "update_form": category_form
    }

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'category update'

    update_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        update_form = ProductCategoryEditForm(request.POST, request.FILES, instance=update_category)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[update_category.pk]))

    else:
        update_form = ProductCategoryEditForm(instance=update_category)

    content = {
        'title': title,
        'update_form': update_form
    }

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'category update'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {
        "title": title,
        "category_to_delete": category
    }

    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'products admin panel'

    category = get_object_or_404(ProductCategory, pk=pk)

    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        "title": title,
        "category": category,
        "objects": products_list
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass