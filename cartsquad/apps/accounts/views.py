from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerRegistrationForm, RetailerRegistrationForm, UserLoginForm, RetailerLoginForm

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Account
from django.contrib.auth.decorators import login_required
from .models import Order

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user.is_retailer = False
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('homepage')
    else:
        form = CustomerRegistrationForm()
    
    return render(request, 'registration_forms/user_signup.html', {'customer_registration_form': form})

def retailer_register(request):
    if request.method == 'POST':
        form = RetailerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user.is_retailer = True
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('homepage')
    #Else, if the request is a GET request, then we will create a new form and render it.
    else:
        form = RetailerRegistrationForm()
    
    return render(request, 'registration_forms/retailer_signup.html', {'retailer_registration_form': form})

def logout_user(request):
    logout(request)
    return redirect('homepage')

def user_login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('homepage')
    
    #If the request is a POST request, then we will create a new form with the data from the POST request and validate it.
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
    #If request is a GET request, then we will create a new form and render it.
    else:
        form = UserLoginForm()
    
    return render(request, 'login_forms/user_login.html', {'user_login_form': form})

def retailer_login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/products/view_all')
    
    #If the request is a POST request, then we will create a new form with the data from the POST request and validate it.
    if request.POST:
        form = RetailerLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                if user.is_retailer == False:
                    return redirect('homepage')
                else:
                    login(request, user)
                    return redirect('/products/view_all')
    #If request is a GET request, then we will create a new form and render it.
    else:
        form = RetailerLoginForm()
    
    return render(request, 'login_forms/retailer_login.html', {'retailer_login_form': form})

def profile_view(request):
    """This view is used to display the profile of the user."""
    user = request.user
    if user.is_authenticated:
        user_profile = {

            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email' : user.email,
            'phone_number' : user.phone_number,
            'date_of_birth' : user.date_of_birth,
            'gender' : user.gender,
            'id': user.user_id,
            'address' : user.address,
            'full_name' : user.full_name


        }
        return render(request, 'login_forms/profile.html', {'user_profile': user_profile})
    else:
        return redirect('homepage')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})

