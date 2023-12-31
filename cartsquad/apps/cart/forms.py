from django import forms 
from .models import Cart

class NewSharedCartForm(forms.ModelForm):
    cart_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Cart Name')
    cart_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Cart Description')
    shared_with = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Shared With',
        help_text= 'Enter up to 10 email addresses, seperated by ; .',
    )

    class Meta:
        model = Cart
        fields = ['cart_name', 'cart_description', 'shared_with']
        widgets = {
            'cart_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cart_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'cart_name': 'Cart Name',
            'cart_description': 'Cart Description',
        }
        help_texts = {
            'shared_with': 'Enter up to 10 email addresses, seperated by ;.',
        }

