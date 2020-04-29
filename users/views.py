from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegister, UserUpdationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from blog.models import Author
from django.core.mail import send_mail

# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        print(' post request ----> ')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print('authenticated')
            login(request, user)
            return redirect('blog-list')
        else:
            print('not authenticated')
            messages.error(request, 'Username or password is correct ')
            return render(request, template_name='users/login.html')

    return render(request, template_name='users/login.html')


def UserLogout(request):
    logout(request)
    return redirect('home')


def register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            messages.success(request, 'Account Created for ',user)
            return redirect('user-login')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, template_name='users/register.html', context=context)


def profile(request, user_id):
    print('profile get request <------')
    instance = request.user.author
    form = UserUpdationForm(instance=instance)
    form.instance.user = request.user
    form.instance.email = request.user.email
    if request.method == 'POST':
        print('profile post request <------')
        form = UserUpdationForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()

    return render(request, template_name='users/profile.html', context={'form': form})
