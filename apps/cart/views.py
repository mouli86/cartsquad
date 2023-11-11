from django.shortcuts import render, redirect
from .models import Cart
from ..products.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required 
def view_cart(request, user_id):
    cart_list = Cart.objects.filter(user_id=user_id)
    query = Product.objects.all().extra(
    select={'quantity': f'SELECT c.quantity FROM products_product p inner join cart_cart c on p.product_id = c.product_id where c.user_id = {user_id}'}
    )
    return render(request, 'cart/view.html', {'products': query})

@login_required 
def add_to_cart(request, prod_id, user_id, quantity):
    products = Product.objects.get(product_id = prod_id)
    print(products.product_stock)
    print(quantity)
    if(products.product_stock >= quantity):
        Cart.atc(request, prod_id, user_id, quantity)
        print('yes')
        return render(request, 'cart/add_cart.html', {'message': 'Added successfully'})
    else:
        return render(request, 'cart/add_cart.html', {'message': f'Available quantity is only {products.product_stock}'})


@login_required 
def delete_from_cart(request, product_id, user_id):
    carts = Cart.objects.all()
    condition1 = {'product_id': product_id}
    condition2 = {'user_id': user_id}
    product_to_be_deleted = Cart.objects.filter(**condition1).filter(**condition2)
    product_to_be_deleted.delete()
    messages.success(request, "Product deleted successfully!")
    return render(request, 'cart/delete_from_cart.html')

