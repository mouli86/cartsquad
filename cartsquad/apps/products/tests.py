from django.test import TestCase
from .models import Product


def test_add_product():
    Product = Product.objects.create(product_name = 'Test Product', product_description = 'Test Description', product_price = 10.00, product_quantity = 10, product_retailer_id = 1)
    assert Product.product_name == 'Test Product'
    assert Product.product_description == 'Test Description'
    assert Product.product_price == 10.00
    assert Product.product_quantity == 10
    assert Product.product_retailer_id == 1

def test_update_product():
    Product = Product.objects.create(product_name = 'Test Product', product_description = 'Test Description', product_price = 10.00, product_quantity = 10, product_retailer_id = 1)
    Product.product_name = 'Updated Product'
    Product.product_description = 'Updated Description'
    Product.product_price = 20.00
    Product.product_quantity = 20
    Product.product_retailer_id = 2
    assert Product.product_name == 'Updated Product'
    assert Product.product_description == 'Updated Description'
    assert Product.product_price == 20.00
    assert Product.product_quantity == 20
    assert Product.product_retailer_id == 2

def test_delete_product():
    Product = Product.objects.create(product_name = 'Test Product', product_description = 'Test Description', product_price = 10.00, product_quantity = 10, product_retailer_id = 1)
    Product.delete()
    assert Product.product_name == ''
    assert Product.product_description == ''
    assert Product.product_price == 0.00
    assert Product.product_quantity == 0
    assert Product.product_retailer_id == 0

def test_view_product():
    Product = Product.objects.create(product_name = 'Test Product', product_description = 'Test Description', product_price = 10.00, product_quantity = 10, product_retailer_id = 1)
    assert Product.product_name == 'Test Product'
    assert Product.product_description == 'Test Description'
    assert Product.product_price == 10.00
    assert Product.product_quantity == 10
    assert Product.product_retailer_id == 1

def test_view_all_products():
    product_1 = Product.objects.create(product_name = 'Test Product', product_description = 'Test Description', product_price = 10.00, product_quantity = 10, product_retailer_id = 1)
    assert product_1.product_name == 'Test Product'
    assert product_1.product_description == 'Test Description'
    assert product_1.product_price == 10.00
    assert product_1.product_quantity == 10
    assert product_1.product_retailer_id == 1

    product_2 = Product.objects.create(product_name = 'Test Product 2', product_description = 'Test Description 2', product_price = 20.00, product_quantity = 20, product_retailer_id = 2)
    assert product_2.product_name == 'Test Product 2'
    assert product_2.product_description == 'Test Description 2'
    assert product_2.product_price == 20.00
    assert product_2.product_quantity == 20
    assert product_2.product_retailer_id == 2

    product_a = Product.objects.all(product_retailer_id = 1)
    product_a.count() == 1
    

    

