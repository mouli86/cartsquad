from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        
        #Required fields
        product_name = forms.CharField(required=True)
        product_price = forms.DecimalField(required=True)   
        product_description = forms.CharField(required=True)

        fields = ['product_name', 'product_price', 'product_description', 'product_image', 'product_category', 'product_stock',
                'product_brand', 'product_status', 'product_discount', 'product_discount_price', 'product_attributes']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_image' : forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'})),
            'product_category': forms.TextInput(attrs={'class': 'form-control'}),
            'product_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'product_status': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'product_discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_discount_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_attributes': forms.TextInput(attrs={'class': 'form-control'}),
            'product_retailer_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'product_name': 'Product Name',
            'product_price': 'Product Price',
            'product_description': 'Product Description',
            'product_image': 'Product Image',
            'product_category': 'Product Category',
            'product_stock': 'Product Stock',
            'product_rating': 'Product Rating',
            'product_brand': 'Product Brand',
            'product_status': 'Product Status',
            'product_discount': 'Product Discount',
            'product_discount_price': 'Product Discount Price',
            'product_attributes': 'Product Attributes',
            'product_retailer_id': 'Product Retailer ID',
        }

    

        




