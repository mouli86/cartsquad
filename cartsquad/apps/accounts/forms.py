from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

from django.contrib.auth import authenticate

#Customer registration form
class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'gender', 'date_of_birth']
        
    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' input'
            else:
                field.widget.attrs['class'] = 'input'


#Retailer registration form
class RetailerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Valid email required." )
    class Meta:
        model = Account  # Retailer registration form using the Account model
        fields = [ 'business_name', 'retailer_name', 'email', 'phone_number', 'retailer_address','password1', 'password2', 'is_retailer']
    
    def __init__(self, *args, **kwargs):
        super(RetailerRegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' input'
            else:
                field.widget.attrs['class'] = 'input'

#User login form
class UserLoginForm(forms.ModelForm):
    meta = Account
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' input'
            else:
                field.widget.attrs['class'] = 'input'

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            user = authenticate(email = email, password = password)
            if user is None:
                raise forms.ValidationError("Please check your email and password and try again.")
            elif user.is_retailer == 1:
                raise forms.ValidationError("Please login through the retailer login form.")
           
        
#Retailer login form
class RetailerLoginForm(forms.ModelForm):
    meta = Account
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email, password = password):
                raise forms.ValidationError("Please check your email and password and try again.")
            
    def __init__(self, *args, **kwargs):
        super(RetailerLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' input'
            else:
                field.widget.attrs['class'] = 'input'
