from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from apps.accounts.models import Account
import datetime as dt
from django.urls import reverse

class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create a user for the retailer
        self.retailer = Account.objects.create_user(email="retailer@g.com", password="retailerpassword", date_of_birth=dt.date(1999, 1, 1))

        # Create a product
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

    # Test product creation
    def test_product_creation(self):
        product = self.product
        self.assertEqual(str(product), "Test Product")
        # Assert other attributes of the product

    def test_add_product(self):
        # Create a new product and add it to the database
        new_product = Product()
        new_product.add_product(
            product_name="New Product",
            product_price=15.99,
            product_description="New product description",
            product_image="new_image.jpg",
            product_category="New Category",
            product_stock=50,
            product_brand="New Brand",
            product_retailer_id=self.retailer,
            product_search_terms="new, product, terms",
            product_discount=0,
            product_discount_price=0
        )
        
        # Retrieve the newly added product from the database
        added_product = Product.objects.get(product_name="New Product")

        # Assert the attributes of the new product
        self.assertEqual(added_product.product_name, "New Product")
        self.assertEqual(added_product.product_price, 15.99)
        self.assertEqual(added_product.product_description, "New product description")
        self.assertEqual(added_product.product_image, "new_image.jpg")
        self.assertEqual(added_product.product_category, "New Category")
        self.assertEqual(added_product.product_stock, 50)
        self.assertEqual(added_product.product_brand, "New Brand")
        self.assertEqual(added_product.product_retailer_id, self.retailer)


    def test_update_product(self):
        # Update the existing product
        self.product.update_product(
            product_name="Updated Product",
            product_price=12.99,
            product_description="Updated product description",
            product_image="updated_image.jpg",
            product_category="Updated Category",
            product_stock=75,
            product_brand="Updated Brand",
            product_retailer_id=self.retailer,
            product_search_terms="updated, product, terms",
        )
        
        # Retrieve the updated product from the database
        updated_product = Product.objects.get(pk=self.product.pk)

        # Assert the attributes of the updated product
        self.assertEqual(updated_product.product_name, "Updated Product")
        self.assertEqual(updated_product.product_price, 12.99)
        self.assertEqual(updated_product.product_description, "Updated product description")
        self.assertEqual(updated_product.product_image, "updated_image.jpg")
        self.assertEqual(updated_product.product_category, "Updated Category")
        self.assertEqual(updated_product.product_stock, 75)
        self.assertEqual(updated_product.product_brand, "Updated Brand")
        self.assertEqual(updated_product.product_retailer_id, self.retailer)


    # Delete dummy user and product objects
    def tearDown(self):
        self.product.delete()
        self.retailer.delete()

    def test_view_all_products_sort_by_price(self):
        # Test sorting products by price on the view
        response = self.client.get(reverse('products:view_all') + '?sort_by=price')
        self.assertEqual(response.status_code, 200)

        page_obj = response.context['page_obj']

        prices = [product.product_price for product in page_obj]
        self.assertEqual(prices, sorted(prices))  # Assert that prices are in ascending order

    def test_view_all_products_sort_by_ratings(self):
        # Test sorting products by ratings on the view
        response = self.client.get(reverse('products:view_all') + '?sort_by=ratings')
        self.assertEqual(response.status_code, 200)

        page_obj = response.context['page_obj']

        ratings = [product.product_rating for product in page_obj if product.product_rating is not None]
        self.assertEqual(ratings, sorted(ratings, reverse=True))  # Assert that ratings are in descending order
