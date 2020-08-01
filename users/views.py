from django.shortcuts import render, redirect
from users.forms import UserProfileRegistrationForm, UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.models import UserProfile
from cart.models import Cart
from django.contrib.auth.admin import User
from django.contrib.auth.backends import BaseBackend

# Create your views here.


@login_required
def simple(request):
    return HttpResponse("Welcome to simple!")


def user_login(request):
    print('here')
    form = UserLoginForm()
    print('here1')
    print(request.method)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data['username'])
            print(form.cleaned_data['password'])
            user = User.objects.filter(username=form.cleaned_data['username']).filter(password=form.cleaned_data['password']).first()
            print(user)
            if user is not None:
                login(request, user)
                print('login success')
                return redirect('core:index')
    return render(request, 'users/login.html', {'form':form})


def register(request):
    form = UserProfileRegistrationForm()
    form_user = UserRegistrationForm()
    registered = False
    if request.method == 'POST':
        form = UserProfileRegistrationForm(request.POST)
        form_user = UserRegistrationForm(request.POST)
        if form.is_valid() and form_user.is_valid():
            user = User(username=form_user.cleaned_data['username'],
                        email=form_user.cleaned_data['email'],
                        password=form_user.cleaned_data['password'])
            user.save()
            cart = Cart(cart_id=user.id)
            cart.save()
            user_profile = UserProfile(user=user,
                                       user_contact=form.cleaned_data['user_contact'],
                                       address=form.cleaned_data['address'],
                                       cart=cart)
            user_profile.save()
            return redirect('users:user_login')
    print(form.errors)
    return render(request, 'users/registration.html', {'form':form, 'form_user':form_user})


@login_required
def logout(request):
    django_logout(request)
    return redirect('core:index')

