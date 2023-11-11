from django.shortcuts import render, redirect
from .models import Orders
from .models import Cart
from ..products.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Importing the custom iterator from models.py
from .models import OrdersIterator

# Decorator to ensure the user is logged in before accessing the view functions.
@login_required
def view_order_history(request, user_id):
    # Retrieve orders for the specified user_id from the Orders model.
    orders = Orders.objects.filter(user_id=user_id)
    
    # Create an iterator for the orders.
    orders_iterator = OrdersIterator(orders)

    # Render the view template with the orders_iterator.
    return render(request, 'orders/view.html', {'orders': orders_iterator})

@login_required
def add_to_orders(request, user_id, order_id):
    # Define conditions for filtering products to be added to orders.
    condition1 = {'product_id': user_id}
    condition2 = {'is_billable': True}

    # Filter products from Cart model based on the defined conditions.
    product_to_be_added = Cart.objects.filter(**condition1).filter(**condition2)
    
    # Loop through the filtered products and add them to the Orders model.
    for res in product_to_be_added:
        record = Orders(
            order_id=order_id,
            user_id=res.user_id,
            product_id=res.product_id,
            quantity=res.quantity,
            per_item_cost=res.per_item_cost,
            total_cost=res.quantity * res.per_item_cost
        )
        record.save()

    # Render the view template for adding to orders.
    return render(request, 'orders/add.html')
