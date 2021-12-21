from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from users.models import User
from mainapp.models import Product, ProductCategory
from users.forms import UserRegistrationForm
from adminapp.forms import UserEditAdminForm, ProductCategoryEditForm, ProductEditForm


class UserListView(ListView):
    model = User
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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

    user_update = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        update_form = UserEditAdminForm(request.POST, request.FILES, instance=user_update)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[user_update.pk]))

    else:
        update_form = UserEditAdminForm(instance=user_update)

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


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'category update'
        return contex


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


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


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


# class ProductCategoryCreateView(CreateView):
#     model = ProductCategory
#     template_name = 'adminapp/category_update.html'
#     success_url = reverse_lazy('admin:categories')
#     fields = '__all__'


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'product create'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {
        "title": title,
        "update_form": product_form,
        "category": category
    }

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'product update'

    product_update = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        update_form = ProductEditForm(request.POST, request.FILES, instance=product_update)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[product_update.pk]))

    else:
        update_form = ProductEditForm(instance=product_update)

    content = {
        'title': title,
        'update_form': update_form,
        'category': product_update.category
    }

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'product update'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))

    content = {
        "title": title,
        "product_to_delete": product
    }

    return render(request, 'adminapp/product_delete.html', content)
