from django.shortcuts import render, redirect
from .forms import ProductForm, NewProductForm
from .models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def add_product(request):
    user = request.user

    if not user.is_authenticated:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('homepage')

    if not user.is_retailer:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('homepage')

    form = NewProductForm(request.POST, request.FILES)
    if form.is_valid():
        # Create an instance of the product without saving it to the database yet
        product = form.save(commit=False)
        # Set the retailer of the product to the currently logged-in user
        product.product_retailer_id = user
        product.save()  
        messages.success(request, "Product added successfully!")
        product = NewProductForm()
    context ={}
    context['product_form']= form
    return render(request, 'products/add.html', {'product_form': form})
    
@login_required 
def update_product(request, product_id):
    if not request.user.is_retailer:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('homepage')
    else:
        product = Product.objects.get(product_id=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, "Product updated successfully!")
                return redirect('products')
        else:
            form = ProductForm(instance=product)
        return render(request, 'products/edit.html', {'product_form': form})

def view_product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    return render(request, 'products/view.html', {'product': product})

@login_required
def delete_product(request, product_id):
    if not request.user.is_retailer:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('homepage')
    else:
        product = Product.objects.get(product_id=product_id)
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('products')

# This view will be used to view all products for a retailer and it will only show products that belong to the retailer that is logged in.
@login_required
def view_all_products(request):
    if not request.user.is_retailer:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('homepage')
    else:
        sort_by = request.GET.get('sort_by', 'name') # Default sorting by product name
        products = Product.objects.filter(product_retailer_id=request.user.user_id)
        #Convert products to a list so that we can use it in the template need to pass paginator once fronend development us completew
        if sort_by == 'price':
         products = products.order_by('product_price')
        elif sort_by == 'ratings':
            products = products.order_by('-product_rating')

        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        products = list(products)
        return render(request, 'products/all.html', {'products': products})

# This view will be used to search for products.
def search_products(request):
    """Search for products based on product name, product description, product category, product brand, and product search terms."""
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(product_description__icontains=query) |
            Q(product_category__icontains=query) |
            Q(product_brand__icontains=query)|
            Q(product_search_terms__icontains=query)
        ).distinct()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
	#Need to pass paginator once frontend is ready
    page_obj = list(products)
    return render(request, 'products/results.html', {'page_obj': page_obj})

 
