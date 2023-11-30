from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from apps.accounts.models import Account
import datetime as dt

class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create a user for the retailer
        self.retailer = Account.objects.create_user(email="retailer@g.com", password="retailerpassword", date_of_birth = dt.date(1999, 1, 1))
        
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
        self.assertEqual(product.product_price, 10.99)
        self.assertEqual(product.product_description, "This is a test product")
        self.assertEqual(product.product_image, "test_image.jpg")
        self.assertEqual(product.product_category, "Test Category")
        self.assertEqual(product.product_stock, 100)
        self.assertEqual(product.product_brand, "Test Brand")
        self.assertEqual(product.product_retailer_id, self.retailer)
        self.assertEqual(product.product_status, True)
        self.assertEqual(product.product_discount, 0)
        self.assertEqual(product.product_discount_price, 0)

    def test_add_product(self):
        product = Product()
        product.add_product(
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
        self.assertEqual(product.product_name, "New Product")
        self.assertEqual(product.product_price, 15.99)
        self.assertEqual(product.product_description, "New product description")
        self.assertEqual(product.product_image, "new_image.jpg")
        self.assertEqual(product.product_category, "New Category")
        self.assertEqual(product.product_stock, 50)
        self.assertEqual(product.product_brand, "New Brand")
        self.assertEqual(product.product_retailer_id, self.retailer)
      

    def test_update_product(self):
        product = self.product
        product.update_product(
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
        self.assertEqual(product.product_name, "Updated Product")
        self.assertEqual(product.product_price, 12.99)
        self.assertEqual(product.product_description, "Updated product description")
        self.assertEqual(product.product_image, "updated_image.jpg")
        self.assertEqual(product.product_category, "Updated Category")
        self.assertEqual(product.product_stock, 75)
        self.assertEqual(product.product_brand, "Updated Brand")
        self.assertEqual(product.product_retailer_id, self.retailer)
     
    #Delete dummy user and product objects
    def tearDown(self):
        self.product.delete()
        self.retailer.delete()

#Reverse is not defined or not explainable mayuk to fix this
# def test_view_all_products_sort_by_price(self):
#     response = self.client.get(reverse('view_all_products') + '?sort_by=price')
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(len(response.context['page_obj']), 2)
#     self.assertEqual(response.context['sort_by'], 'price')

# def test_view_all_products_sort_by_ratings(self):
#     response = self.client.get(reverse('view_all_products') + '?sort_by=ratings')
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(len(response.context['page_obj']), 2)
#     self.assertEqual(response.context['sort_by'], 'ratings')


    

    

