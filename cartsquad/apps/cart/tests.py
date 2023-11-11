from django.test import TestCase
from django.urls import reverse
from apps.accounts.models import Account
from apps.products.models import Product
from . import views
from .models import Cart
import datetime as dt

class CartModelTest(TestCase):
    def setUp(self):
        self.user =Account.objects.create_user(
           email="user@g.com", password="userpass", date_of_birth = dt.date(1999, 1, 1)
        )
        self.retailer = Account.objects.create_user(email="retailer@g.com", password="retailerpassword", date_of_birth = dt.date(1999, 1, 1))

        self.product = Product.objects.create(
           product_name="Test Product",
            product_price=10.99,
            product_description="This is a test product",
            product_image="test_image.jpg",
            product_category="Test Category",
            product_stock=100,
            product_brand="Test Brand",
            product_retailer_id=self.retailer, 
            product_discount=0,
            product_discount_price=0
        )
        self.cart = Cart.objects.create(
            cart_owner_id=self.user
        )

    def test_cart_creation(self):
        self.assertEqual(self.cart.cart_owner_id, self.user)
        self.assertEqual(self.cart.cart_total, 0)
        self.assertEqual(self.cart.cart_status, True)

    def test_save_to_cart(self):
        self.cart.add_to_cart(self.product.product_id, 2)
        self.assertEqual(len(self.cart.cart_products), 1)
        self.assertEqual(self.cart.cart_products[str(self.product.product_id)]['quantity'], 2)
        self.assertEqual(self.cart.cart_total, 20.0)

    def test_remove_from_cart(self):
        self.cart.add_to_cart(self.product.product_id, 2)
        self.cart.remove_from_cart(self.product.product_id)
        self.assertEqual(len(self.cart.cart_products), 0)
        self.assertEqual(self.cart.cart_total, 0)

    def test_clear_cart(self):
        self.cart.save_to_cart(self.product.product_id, 2)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.cart_products), 0)
        self.assertEqual(self.cart.cart_total, 0)

    def test_checkout(self):
        self.cart.checkout()
        self.assertEqual(self.cart.cart_status, False)
    
    def tearDown(self) -> None:
        return super().tearDown()