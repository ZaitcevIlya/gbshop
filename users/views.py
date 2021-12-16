from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'GeekShop - Authorisation',
        'form': form,
        'next': next
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {'title': 'GeekShop - Registration', 'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
