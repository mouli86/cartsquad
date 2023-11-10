from django.shortcuts import render, redirect
from .models import Orders
from .models import Cart
from ..products.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required 
def view_order_history(request, user_id):
    cart_list = Orders.objects.filter(user_id=user_id)
    return render(request, 'orders/view.html', {'products': cart_list})

@login_required 
def add_to_orders(request, user_id, order_id):
    condition1 = {'product_id': user_id}
    condition2 = {'is_billable': True}
    product_to_be_added = Cart.objects.filter(**condition1).filter(**condition2)
    for res in product_to_be_added:
        record = Orders(order_id=order_id, user_id=res.user_id, product_id=res.product_id, quantity=res.quantity, per_item_cost = res.per_item_cost, total_cost = res.quantity * res.per_item_cost)
        record.save()
    return render(request, 'orders/add.html')

