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
    return redirect('products:view_product', product_id=product_id)


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
def remove_from_cart(request, product_id, cart_id = None):
    user = request.user
    #If cart_id is passed, then remove from shared cart
    if cart_id:
        cart = Cart.objects.get(cart_id=cart_id, cart_status=True, shared_cart=True)
        if cart:
            cart.remove_from_cart(product_id)
            cart.save()
        return redirect('cart:view_shared_cart', cart_id=cart_id)
    else:
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
def delete_shared_cart(request, cart_id):
    user = request.user
    cart = Cart.objects.filter(
        cart_owner_id=user, cart_status=True, shared_cart=True, cart_id=cart_id)
    # delete the cart if the user is the owner of the cart
    if cart:
        cart = cart[0]
        cart.delete()

    return redirect('cart:shared_carts')


@login_required
def create_shared_cart(request):
    """This function creates a shared cart for the user. 
    This is used when the user wants to share the cart with other users."""
    if request.method == 'POST':
        form = NewSharedCartForm(request.POST)
        user = request.user
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
            cart.shared_with[user.user_id] = {
                    'email': user.email, 'accepted': 1, 'name': user.first_name + " " + user.last_name}
            cart.cart_total = 0.0
            for email in emails:
                email = email.strip()
                # Remove leadind and trailing ';'
                email = email.strip(';')
                # check if the text is valid email
                if Account.objects.filter(email=email).exists():
                    account_id = Account.objects.get(email=email).user_id
                    user_name = Account.objects.get(
                        email=email).first_name + " " + Account.objects.get(email=email).last_name
                    if account_id not in cart.shared_with:
                        cart.shared_with[account_id] = {
                            'email': email, 'accepted': 0, 'name': user_name}
                else:
                    print(email + " : User not found")
            cart.save()
            cart = NewSharedCartForm()
            messages.success(request, "Shared cart created successfully!")
            return redirect('cart:shared_carts')
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

    owned_shared_carts = Cart.objects.filter(Q(shared_cart=True)
                                             & Q(cart_owner_id=user)
                                             & Q(cart_status=True))

    return render(request, 'cart/shared_carts.html', {'shared_carts': owned_shared_carts, 'accepted_shared_carts': accepted_shared_carts, 'pending_shared_carts': pending_shared_carts})

@login_required
def view_accepted_shared_carts(request):
    """This function is used to view the accepted shared cart in products page only."""
    user = request.user
    accepted_shared_carts = Cart.objects.filter(
        Q(shared_with__contains={user.user_id: {'accepted': 1}}) &
        Q(cart_status=True) &
        Q(shared_cart=True)
    ).exclude(shared_with={user.user_id: {'accepted': 0}})
    return render(request, 'cart/accepted_shared_carts.html', {'accepted_shared_carts': accepted_shared_carts})

@login_required
def accept_shared_cart(request, cart_id):
    """This function is used to accept the shared cart."""
    user = request.user
    cart = Cart.objects.get(cart_id=cart_id)
    cart.shared_with[str(user.user_id)]['accepted'] = 1
    cart.save()
    return redirect('cart:shared_carts')


@login_required
def update_shared_cart(request, cart_id):
    """This function is used to update the shared cart."""
    user = request.user
    cart = Cart.objects.get(cart_id=cart_id)
    # check if the user is the owner of the cart and populate the form with existing data

    if cart.cart_owner_id == user:
        if request.method == 'POST':
            form = NewSharedCartForm(request.POST)
            if form.is_valid():
                cart.cart_name = form.cleaned_data['cart_name']
                cart.cart_description = form.cleaned_data['cart_description']
                shared_with = form.cleaned_data['shared_with']
                emails = shared_with.split(';')
                cart.shared_cart = True
                cart.status = True
                cart.shared_with = {}
                cart.shared_with[user.user_id] = {
                    'email': user.email, 'accepted': 1, 'name': user.first_name + " " + user.last_name}
                cart.cart_total = 0.0
                for email in emails:
                    email = email.strip()
                    if Account.objects.filter(email=email).exists():
                        account_id = Account.objects.get(email=email).user_id
                        print(account_id)
                        user_name = Account.objects.get(
                            email=email).first_name + " " + Account.objects.get(email=email).last_name
                        print(user_name)
                        if account_id not in cart.shared_with:
                            cart.shared_with[account_id] = {
                                'email': email, 'accepted': 0, 'name': user_name}
                    else:
                        print(email + " : User not found")
                cart.save()
                cart = NewSharedCartForm()
                messages.success(request, "Shared cart updated successfully!")
                return redirect('cart:shared_carts')
            else:
                messages.error(request, "Error in the form submission.")
        emails = ""
        for email in cart.shared_with:
            emails += cart.shared_with[email]['email'] + ";"
        form = NewSharedCartForm(initial={
                                 'cart_name': cart.cart_name, 'cart_description': cart.cart_description, 'shared_with': emails})
        return render(request, 'cart/shared_cart_form.html', {'shared_cart_form': form})

@login_required
def add_to_shared_cart(request, cart_id, product_id, comment=""):

    """This function is used to add the product to the shared cart."""
    user = request.user
    cart = Cart.objects.get(cart_id=cart_id)
    user_name = user.first_name + " " + str(user.last_name)[0]
    
    if cart:
        cart.save_to_cart(product_id, user_name, comment, 1)
        cart.save()
    
    return redirect('products:view_product', product_id=product_id)

@login_required
def view_shared_cart(request, cart_id):
    """This function is used to view the shared cart."""
    user = request.user
    cart = Cart.objects.get(cart_id=cart_id)
    can_checkout = True if cart.cart_owner_id == user else False
    cart_data = []
    if cart:
        if cart.cart_products in [None, {}]:
            cart.cart_products = {}
            cart.save()
        for product_id in cart.cart_products:
            product = Product.objects.get(product_id=product_id)
            cart_data.append({
                'product_id': product_id,
                'product_name': product.product_name,
                'product_price': product.product_price,
                'quantity': cart.cart_products[product_id]['quantity'],
                'total_price': product.product_price * cart.cart_products[product_id]['quantity'],
                'comment': cart.cart_products[product_id]['comment'],
                'added_by': cart.cart_products[product_id]['added_by']
            })
        
    return render(request, 'cart/view_shared_cart.html', {'cart_data': cart_data, 'cart_total': cart.cart_total, 'cart': cart.cart_id, 'checkout': can_checkout})

@login_required
def remove_from_shared_cart(request, cart_id, product_id):
    """This function is used to remove the product from the shared cart."""
    user = request.user
    cart = Cart.objects.get(cart_id=cart_id)
    if cart:
        cart.remove_from_cart(product_id)
        cart.save()
    return redirect('cart:view_shared_cart', cart_id=cart_id)

