from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from .forms import UserRegistrationForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегeстрировались')
            return HttpResponseRedirect(reverse('login'))

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(request.POST)
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
        context = {
            'form': form,
        }
    return render(request, 'users/login.html', context=context)
