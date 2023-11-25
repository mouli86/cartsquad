from django.db import models
import datetime as dt
from apps.products.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    cart_products = models.JSONField(null=True, blank=True)
    cart_total = models.DecimalField(decimal_places=2, max_digits=10)
    cart_date_created = models.DateField()
    cart_owner_id = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    
    #For shared cart functionality
    shared_cart = models.BooleanField(default=False)
    shared_with = models.JSONField(null=True, blank=True)
    cart_name = models.CharField(max_length=100, null=True, blank=True)
    cart_description = models.TextField(null=True, blank=True)
    
    
    #This is will disabled once cart is checkout and order is placed
    cart_status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cart_id)
    
    def save(self, *args, **kwargs):
        self.cart_date_created = dt.date.today()
        super(Cart, self).save(*args, **kwargs)

    def update_cart_total(self):
        total = 0
        for product in self.cart_products.values():
            total += product['price'] * product['quantity']
        self.cart_total = total
        self.save()

    def save_to_cart(self, product_id, user = '', comment = '', quantity=1):
        if not self.cart_products:
            self.cart_products = {}

        product = Product.objects.get(product_id=product_id)

        if str(product_id) in self.cart_products:
            cart_item = self.cart_products[str(product_id)]
            cart_item['quantity'] += quantity
        else:
            self.cart_products[str(product_id)] = {
                'name': product.product_name,
                'price': float(product.product_price),
                'quantity': quantity,
                'added_by': user,
                'comment': comment
            }
        
        self.update_cart_total()
    
    def remove_from_cart(self, product_id):
        if self.cart_products and str(product_id) in self.cart_products:
            del self.cart_products[str(product_id)]
        else:
            return
        self.update_cart_total()
        self.save()

    def clear_cart(self):
        self.cart_products = {}
        self.cart_total = 0
        self.save()

    def checkout(self):
        self.cart_status = False
        self.save()

    def update_cart(self, product_id, quantity):
        if self.cart_products and str(product_id) in self.cart_products:
            self.cart_products[str(product_id)]['quantity'] = quantity
        else:
            return
        self.update_cart_total()
        self.save()    
        