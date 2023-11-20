from django.shortcuts import render
from .models import Cart
from apps.accounts.models import Account
from apps.products.models import Product
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewSharedCartForm
from django.db.models import Q


@login_required
def add_to_cart(request, product_id, quantity=1):
    user = request.user

    # Get list of all active cart objects for the user
    cart = Cart.objects.filter(
        cart_owner_id=user, cart_status=True, shared_cart=False)
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
    cart = Cart.objects.filter(
        cart_owner_id=user, cart_status=True, shared_cart=False)
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
    cart = Cart.objects.filter(
        cart_owner_id=user, cart_status=True, shared_cart=False)
    if cart:
        cart = cart[0]
        cart.remove_from_cart(product_id)
        cart.save()
    return redirect('cart:view_cart')


@login_required
def update_quantity(request, product_id):
    user = request.user
    quantity = request.POST.get('quantity')
    cart = Cart.objects.filter(
        cart_owner_id=user, cart_status=True, shared_cart=False)
    if cart:
        cart = cart[0]
        cart.update_cart(product_id, int(quantity))
        cart.save()
    return redirect('cart:view_cart')


@login_required
def create_shared_cart(request):
    """This function creates a shared cart for the user. 
    This is used when the user wants to share the cart with other users."""
    if request.method == 'POST':
        form = NewSharedCartForm(request.POST)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.cart_owner_id = request.user
            cart.cart_name = form.cleaned_data['cart_name']
            cart.cart_description = form.cleaned_data['cart_description']
            shared_with = form.cleaned_data['shared_with']
            emails = shared_with.split(';')
            cart.shared_cart = True
            cart.status = True
            cart.shared_with = {}
            cart.cart_total = 0.0
            for email in emails:
                email = email.strip()
                # Remove leadind and trailing ';'
                email = email.strip(';')
                # check if the text is valid email
                if Account.objects.filter(email=email).exists():
                    account_id = Account.objects.get(email=email).user_id
                    print(account_id)
                    user_name = Account.objects.get(
                        email=email).first_name + " " + Account.objects.get(email=email).last_name[0]
                    print(user_name)
                    if account_id not in cart.shared_with:
                        cart.shared_with[account_id] = {
                            'email': email, 'accepted': 0, 'name': user_name}
                else:
                    print(email + " : User not found")
            cart.save()
            cart = NewSharedCartForm()
            messages.success(request, "Shared cart created successfully!")
        else:
            messages.error(request, "Error in the form submission.")

    form = NewSharedCartForm()
    return render(request, 'cart/shared_cart_form.html', {'shared_cart_form': form})


@login_required
def view_shared_carts(request):
    """This function is used to view the shared cart."""
    user = request.user

    accepted_shared_carts = Cart.objects.filter(
        Q(shared_with__contains={user.user_id: {'accepted': 1}}) &
        Q(cart_status=True) &
        Q(shared_cart=True)
    ).exclude(shared_with={user.user_id: {'accepted': 0}})

    pending_shared_carts = Cart.objects.filter(
        Q(shared_with__contains={user.user_id: {'accepted': 0}}) &
        Q(cart_status=True) &
        Q(shared_cart=True)
    )

    owned_shared_carts = Cart.objects.filter(Q(shared_cart = True)
                                             & Q(cart_owner_id=user)
                                             & Q(cart_status = True))
  

    return render(request, 'cart/shared_carts.html', {'shared_carts': owned_shared_carts, 'accepted_shared_carts': accepted_shared_carts, 'pending_shared_carts': pending_shared_carts})

