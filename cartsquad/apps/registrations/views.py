# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, RetailerRegistrationForm

# View for rendering the 'index.html' template
def index(request):
    return render(request, 'index.html')

# View for handling user registration
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user registration data if the form is valid
            # Additional logic can be added here, such as redirecting to a thank-you page or login page.
            return redirect('login')
    else:
        form = UserRegistrationForm()
    # Render the 'register_user.html' template and pass the form for user registration
    return render(request, 'register_user.html', {'form': form})

# View for handling retailer registration
def register_retailer(request):
    if request.method == 'POST':
        form = RetailerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save retailer registration data if the form is valid
            # Additional logic can be added here.
            return redirect('login')
    else:
        form = RetailerRegistrationForm()
    # Render the 'register_retailer.html' template and pass the form for retailer registration
    return render(request, 'register_retailer.html', {'form': form})
