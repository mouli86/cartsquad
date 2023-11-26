from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.accounts.models import Account
from apps.products.models import Product
from .models import Cart
import datetime as dt

class CartModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@g.com',
            password='testpass',
            date_of_birth=dt.date(1999, 1, 1))

        self.retailer = Account.objects.create_user(
            email="retailer@g.com",
            password="retailerpassword",
            date_of_birth=dt.date(1999, 1, 1))

        self.product = Product.objects.create(
            product_name="Test Product",
            product_price=10,
            product_description="This is a test product",
            product_image="test_image.jpg",
            product_category="Test Category",
            product_stock=100,
            product_brand="Test Brand",
            product_retailer_id=self.retailer, 
            product_discount=0,
            product_discount_price=0
        )

    def test_cart_creation(self):
        cart = Cart.objects.create(
            cart_owner_id=self.user,
            cart_products={},
            cart_total=0.0
        )
        
        self.assertIsNotNone(cart.cart_date_created)

    def test_add_to_cart(self):
        cart = Cart.objects.create(cart_owner_id=self.user, shared_cart=False, cart_status=True, cart_total=0.0, cart_products={}, cart_date_created=dt.date.today())
        cart.save_to_cart(self.product.product_id, quantity=2)
        self.assertEqual(len(cart.cart_products), 1)
        self.assertEqual(cart.cart_total, 20.0)

    def test_remove_from_cart(self):
        cart = Cart.objects.create(cart_owner_id=self.user, shared_cart=False, cart_status=True, cart_total=0.0, cart_products={}, cart_date_created=dt.date.today())
        cart.save_to_cart(self.product.product_id, quantity=2)
        cart.remove_from_cart(self.product.product_id)
        self.assertEqual(len(cart.cart_products), 0)
        self.assertEqual(cart.cart_total, 0.0)

    def test_update_cart(self):
        cart = Cart.objects.create(cart_owner_id=self.user, shared_cart=False, cart_status=True, cart_total=0.0, cart_products={}, cart_date_created=dt.date.today())
        cart.save_to_cart(self.product.product_id, quantity=2)
        cart.update_cart(self.product.product_id, quantity=3)
        self.assertEqual(cart.cart_products[str(self.product.product_id)]['quantity'], 3)
        self.assertEqual(cart.cart_total, 30.0)

    
    def tearDown(self) -> None:
        return super().tearDown()

    
    def test_clear_cart(self):
        cart = Cart.objects.create(cart_owner_id=self.user, shared_cart=False, cart_status=True, cart_total=0.0, cart_products={}, cart_date_created=dt.date.today())
        cart.save_to_cart(self.product.product_id, quantity=2)
        cart.clear_cart()
        self.assertEqual(len(cart.cart_products), 0)
        self.assertEqual(cart.cart_total, 0.0)

    def test_checkout_cart(self):
        cart = Cart.objects.create(cart_owner_id=self.user, shared_cart=False, cart_status=True, cart_total=0.0, cart_products={}, cart_date_created=dt.date.today())
        cart.save_to_cart(self.product.product_id, quantity=2)
        cart.checkout()
        self.assertFalse(cart.cart_status)

    def test_shared_cart(self):
        # Create two users and a shared cart
        user2 = get_user_model().objects.create_user(
            email='testuser2@g.com',
            password='testpass2',
            date_of_birth=dt.date(1999, 1, 1))

        cart = Cart.objects.create(cart_owner_id=self.user, shared_cart=True, cart_status=True, cart_total=0.0, cart_products={}, cart_date_created=dt.date.today())
        cart.shared_with = [user2.id]
        cart.save_to_cart(self.product.product_id, quantity=2)

        # Check if the shared user has the same product in their cart
        shared_user_cart = Cart.objects.filter(cart_owner_id=user2, shared_cart=True, cart_status=True)
        self.assertTrue(shared_user_cart.exists())
        shared_user_cart = shared_user_cart[0]
        self.assertEqual(len(shared_user_cart.cart_products), 1)
        self.assertEqual(shared_user_cart.cart_total, 20.0)
