from django.shortcuts import render
from .models import Cart
from apps.products.models import Product
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id, quantity=1):
    user = request.user

    #Get list of all active cart objects for the user
    cart = Cart.objects.filter(cart_owner_id=user, cart_status=True, shared_cart=False)
    if cart:
        cart = cart[0]
        cart.save_to_cart(product_id, quantity)
        cart.save()
    else:
       cart = Cart(cart_owner_id=user)
       cart.save_to_cart(product_id, quantity)
       cart.save()
    messages.success(request, "Product added to cart successfully!")
    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    user = request.user
    cart = Cart.objects.filter(cart_owner_id=user, cart_status=True, shared_cart=False)
    cart.cart_total = 0.0
    cart_data = []
    if cart:
        cart = cart[0]
        for product_id in cart.cart_products:
            product = Product.objects.get(product_id=product_id)
            cart_data.append({
                'product_id': product_id,
                'product_name': product.product_name,
                'product_price': product.product_price,
                'quantity': cart.cart_products[product_id]['quantity'],
                'total_price': product.product_price * cart.cart_products[product_id]['quantity']
            })
       
    return render(request, 'cart/view_cart.html', {'cart_data': cart_data, 'cart_total': cart.cart_total})

@login_required
def remove_from_cart(request, product_id):
    user = request.user
    cart = Cart.objects.filter(cart_owner_id=user, cart_status=True, shared_cart=False)
    if cart:
        cart = cart[0]
        cart.remove_from_cart(product_id)
        cart.save()
    return redirect('cart:view_cart')


@login_required
def update_quantity(request, product_id):
    user = request.user
    quantity = request.POST.get('quantity')
    cart = Cart.objects.filter(cart_owner_id=user, cart_status=True, shared_cart=False)
    if cart:
        cart = cart[0]
        cart.update_cart(product_id, int(quantity))
        cart.save()
    return redirect('cart:view_cart')




