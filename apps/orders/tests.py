from django.test import TestCase
from django.urls import reverse
from .models import Orders
from .views import OrdersIterator
from datetime import date
from decimal import Decimal

class OrdersTestCase(TestCase):
    # Setting up initial data for testing
    def setUp(self):
        Orders.objects.create(
            order_id=1,
            user_id=101,
            product_id=201,
            quantity=3,
            per_item_cost=Decimal('10.00'),
            total_cost=Decimal('30.00')
        )

    # Test the __str__ method of the Orders model
    def test_orders_model_str_method(self):
        order = Orders.objects.get(order_id=1)
        self.assertEqual(str(order), "201, 101, 1")

    # Test the save method of the Orders model
    def test_orders_model_save_method(self):
        order = Orders.objects.get(order_id=1)
        today = date.today()
        self.assertEqual(order.product_date_modified, today)
        self.assertEqual(order.product_date_added, today)
        self.assertTrue(order.product_status)

    # Test the custom iterator for Orders
    def test_orders_iterator(self):
        orders = Orders.objects.all()
        orders_iterator = OrdersIterator(orders)
        result = [order for order in orders_iterator]
        self.assertEqual(len(result), 1)

    # Test the view_order_history view function
    def test_view_order_history(self):
        response = self.client.get(reverse('orders:view_order_history', args=(101,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "201, 101, 1")

    # Test the add_to_orders view function
    def test_add_to_orders(self):
        # Simulate a request to add an order to the cart
        cart_response = self.client.get(reverse('orders:add_to_orders', args=(101, 1)))
        self.assertEqual(cart_response.status_code, 200)

        # Retrieve the added order from the database and check its attributes
        order = Orders.objects.get(order_id=1)
        self.assertEqual(order.user_id, 101)
        self.assertEqual(order.product_id, 201)
        self.assertEqual(order.quantity, 3)
        self.assertEqual(order.per_item_cost, Decimal('10.00'))
        self.assertEqual(order.total_cost, Decimal('30.00'))
