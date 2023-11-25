from django.shortcuts import render, redirect
from .models import Orders
from apps.cart.models import Cart
from ..products.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime as dt

# Importing the custom iterator from models.py
from .models import OrdersIterator

# Decorator to ensure the user is logged in before accessing the view functions.
@login_required
def view_order_history(request):
    user_id = request.user
    # Retrieve orders for the specified user_id from the Orders model.
    orders = Orders.objects.filter(user_id=user_id)

    # Create an iterator for the orders.
    orders_iterator = OrdersIterator(orders)

    # Render the view template with the orders_iterator.
    return render(request, 'orders/order_history.html', {'orders': orders_iterator})

@login_required
def checkout(request):
    user = request.user
    cart = Cart.objects.get(
        cart_owner_id=user, cart_status=True, shared_cart=False)
    order = Orders(user_id=user, products=cart.cart_products,
                   order_total=cart.cart_total)
    order.order_date_created = dt.date.today()
    order.shipping_address = user.address
    order.billing_address = user.address
    order.products = cart.cart_products
    order.payment_method = "COD"
    cart.cart_status = False
    for product in cart.cart_products:
        print(product)
        product = Product.objects.get(product_id=product)
        product.product_stock = product.product_stock - \
            cart.cart_products[str(product.product_id)]['quantity']
        product.save()
    order.save()
    cart.save()
    return render(request, 'orders/order_summary.html', {'order': order})


@login_required
def view_order(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    products_list = {}
    # Convert the products from a string to a dictionary
    print(type(order.products))
    for i in order.products:
        product = Product.objects.get(product_id=i)
        products_list[i] = {}
        products_list[i]['product_obj'] = product
        products_list[i]['price'] = order.products[i]['price']
        products_list[i]['quantity'] = order.products[i]['quantity']
        products_list[i]['sub_total'] = order.products[i]['price'] * \
            order.products[i]['quantity']
    order.products = products_list
    return render(request, 'orders/view_order.html', {'order': order})
