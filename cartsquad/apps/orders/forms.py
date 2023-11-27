from django import forms
from .models import Orders

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['shipping_address', 'billing_address', 'payment_method']
        widgets = {
            'shipping_address': forms.Textarea(attrs={'class': 'form-control'}),
            'billing_address': forms.Textarea(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'shipping_address': 'Shipping Address',
            'billing_address': 'Billing Address',
            'payment_method': 'Payment Method',
        }
        help_texts = {
            'payment_method': 'Select a payment method.',
        }
        # Add choices for the payment method
        choices = [
            ('credit', 'Credit Card'),
            ('debit', 'Debit Card'),
            ('cash_on_delivery', 'Cash on Delivery'),
        ]
        widgets = {
            'payment_method': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }
