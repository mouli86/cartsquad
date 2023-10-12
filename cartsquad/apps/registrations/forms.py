from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # User registration form using the CustomUser model
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'gender', 'date_of_birth']

class RetailerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Retailer registration form using the CustomUser model
        fields = ['business_name', 'address', 'phone_number', 'email']
