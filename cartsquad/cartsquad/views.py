from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, RetailerRegistrationForm

def index(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic can be added here, like redirecting to a thank you page or login page.
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register_user.html', {'form': form})

def register_retailer(request):
    if request.method == 'POST':
        form = RetailerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic can be added here.
            return redirect('login')
    else:
        form = RetailerRegistrationForm()
    return render(request, 'register_retailer.html', {'form': form})
