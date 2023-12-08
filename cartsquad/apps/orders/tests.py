import uuid
from django.test import TestCase
from django.urls import reverse
from .models import Orders
from .views import OrdersIterator
from datetime import date
from decimal import Decimal
from django.contrib.auth import get_user_model
from apps.cart.models import Cart
from apps.accounts.models import Account

class OrdersTestCase(TestCase):
    def setUp(self):
        self.order1_id = uuid.uuid4()
        self.order2_id = uuid.uuid4()
        self.order3_id = uuid.uuid4()
        self.user1 = Account.objects.create_user(
            email="user1@cs.com",
            password="user1password",
            date_of_birth=date.today()
        )
        self.user2 = Account.objects.create_user(
            email="user2@cs.com",
            password="user2password",
            date_of_birth=date.today()
        )
        Orders.objects.create(
            #Create a new uuid for each order
            order_id= self.order1_id,
            order_date_created=date.today(),
            order_total=Decimal('10.00'),
            shipping_address="123 Main St",
            billing_address="123 Main St",
            delivered=False,
            payment_method="Credit Card",
            user_id=self.user1,
            products=[{"product_id": "1", "quantity": 1}]
        )
        Orders.objects.create(
            order_id=self.order2_id,
            order_date_created=date.today(),
            order_total=Decimal('20.00'),
            shipping_address="123 Main St",
            billing_address="123 Main St",
            delivered=False,
            payment_method="Debit Card",
            user_id=self.user2,
            products=[{"product_id": "2", "quantity": 2}]
        )
        Orders.objects.create(
            order_id=self.order3_id,
            order_date_created=date.today(),
            order_total=Decimal('30.00'),
            shipping_address="124 Main St",
            billing_address="124 Main St",
            delivered=False,
            payment_method="Cash",
            user_id=self.user1,
            products=[{"product_id": "3", "quantity": 1}]
        )

    def test_orders(self):
        """Orders are correctly identified"""
        order1 = Orders.objects.get(order_id=self.order1_id)
        order2 = Orders.objects.get(order_id=self.order2_id)
        self.assertEqual(order1.order_total, Decimal('10.00'))
        self.assertEqual(order2.order_total, Decimal('20.00'))

    def test_orders_iterator(self):
        """Orders iterator returns correct number of orders"""
        orders = Orders.objects.filter(user_id=self.user1)
        orders_iterator = OrdersIterator(orders)
        self.assertEqual(len(orders_iterator.orders), 2)

    def test_orders_view(self):
        """Orders view returns correct number of orders for a user"""
        self.client.login(email="user1@cs.com", password="user1password")
        response = self.client.get(reverse('orders:order_history'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['orders'].orders), 2)
    