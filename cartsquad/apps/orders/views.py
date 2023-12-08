from django.shortcuts import render, redirect
from .models import Orders
from apps.cart.models import Cart
from ..products.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime as dt
from .forms import CheckOutForm

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
def checkout(request, cart_id = None):
    user = request.user
    # Pass shared cart id if it exists to the checkout view else pass the user id to get user personal cart
    if cart_id is None:
        cart = Cart.objects.get(cart_owner_id=user, cart_status=True, shared_cart=False)
        order = Orders(user_id=user, products=cart.cart_products, order_total=cart.cart_total)
    else:
        cart = Cart.objects.get(cart_id=cart_id)
        order = Orders(user_id=user, products=cart.cart_products, order_total=cart.cart_total, shared_order=True)

    
    order.order_date_created = dt.date.today()
    order_form = CheckOutForm(request.POST or None, instance=order)
    
    if request.method == 'POST':
        if order_form.is_valid():
            order.billing_address = order_form.cleaned_data['billing_address']
            order.shipping_address = order_form.cleaned_data['shipping_address']
            order.payment_method = order_form.cleaned_data['payment_method']
            messages.success(request, "Order placed successfully!")
            order.products = cart.cart_products
            cart.cart_status = False
            order_form = CheckOutForm()

            # Iterate through the products in the cart and update the product stock from the current order
            for product_id, product_data in cart.cart_products.items():
                product = Product.objects.get(product_id=product_id)
                product.product_stock -= product_data['quantity']
                product.save()
            order.save()
            cart.save()
            return redirect('orders:view_order', order_id=order.order_id)
    
    return render(request, 'orders/checkout_form.html', {'order_form': order_form, 'cart': cart})


@login_required
def view_order(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    products_list = {}
    # Convert the products from a string to a dictionary
    for i in order.products:
        product = Product.objects.get(product_id=i)
        products_list[i] = {}
        products_list[i]['product_obj'] = product
        products_list[i]['price'] = order.products[i]['price']
        products_list[i]['quantity'] = order.products[i]['quantity']
        products_list[i]['sub_total'] = order.products[i]['price'] * order.products[i]['quantity']
    order.products = products_list
    return render(request, 'orders/view_order.html', {'order': order})
