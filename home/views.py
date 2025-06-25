from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

def landing(request):
    return render(request, 'home/landing.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})
