from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Task

def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing/landing.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if User.objects.filter(username=username).exists():
            return render(request, 'landing/signup.html', {'message': 'Username already taken!'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'landing/signup.html', {'message': 'Email already registered!'})
        elif password != confirm_password:
            return render(request, 'landing/signup.html', {'message': 'Passwords do not match!'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Redirect to login page after success

    return render(request, 'landing/signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # change this to your dashboard/home page
        else:
            return render(request, 'landing/login.html', {'message': 'Invalid credentials!'})

    return render(request, 'landing/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    selected_date = request.GET.get('date')
    if selected_date:
        tasks = Task.objects.filter(user=request.user, due_date=selected_date)
    else:
        tasks = Task.objects.filter(user=request.user)

    return render(request, 'main/dashboard.html', {
        'now': now(),
        'tasks': tasks
    })

@login_required
def tasks_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/tasks.html')
@login_required
def expenses_view(request):
    if not request.user.is_authenticated:
        return redirect('main/expenses.html')