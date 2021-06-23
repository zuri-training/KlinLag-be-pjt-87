from django.shortcuts import render, redirect
from .forms import UserSignUpForm, AgencySignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def signup_user(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_giver = True
            login(request, user)
            return redirect('main_app:home')
    else:
        form = UserSignUpForm
    return render(request, 'signup_user.html', {'signup_user_form': form})


def signup_agency(request):
    if request.method == 'POST':
        form = AgencySignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_collector = True
            login(request, user)
            return redirect('main_app:home')
    else:
        form = AgencySignUpForm
    return render(request, 'signup_agency.html', {'signup_agency_form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('main_app:home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main_app:login")


def index(request):
    return render(request, 'index.html')


def landing(request):
    return render(request, 'landing.html')
