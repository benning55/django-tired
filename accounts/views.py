from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import dayoff
from .forms import UserRegisterForm, DayOffForm


def mylogin(request, user):
    context = {}
    if request.POST:
        username = request.POST.get('username')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now can login {username}!')
            return redirect('/login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def home(request):
    data = dayoff.objects.all()
    return render(request, 'accounts/home.html', {'data': data})


def dayoffSend(request):
    if request.method == 'POST':
        form = DayOffForm(request.POST)
        if form.is_valid():
            dayoff.objects.create(
                reason=form.cleaned_data.get('reason'),
                type=form.cleaned_data.get('type'),
                date_start=form.cleaned_data.get('date_start'),
                date_end=form.cleaned_data.get('date_end'),
                create_by=User.objects.get(username=request.user.username),
                approve_status='3',
            )
            return redirect('home')
    else:
        form = DayOffForm()
    return render(request, 'accounts/dayoff.html', {'form': form})

