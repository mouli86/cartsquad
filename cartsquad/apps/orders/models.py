from django.db import models
import datetime as dt
import uuid

class Orders(models.Model):
    """
    Represents an order placed by a user.

    Attributes:
        order_id (UUIDField): The unique identifier for the order.
        user_id (ForeignKey): The foreign key to the user's account.
        products (JSONField): The JSON field to store the products in the order.
        order_total (DecimalField): The total amount of the order.
        order_date_created (DateField): The date when the order was created.
        shipping_address (CharField): The shipping address for the order.
        billing_address (CharField): The billing address for the order.
        payment_method (CharField): The payment method used for the order.
        delivered (BooleanField): Indicates whether the order has been delivered or not.
        shared_order (BooleanField): Indicates whether the order is shared or not.
        shared_with (JSONField): The JSON field to store the users with whom the order is shared.

    Methods:
        __str__(): Returns a string representation of the Orders instance.
    """

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    user_id = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    products = models.JSONField(null=True, blank=True)
    order_total = models.DecimalField(decimal_places=2, max_digits=10)
    order_date_created = models.DateField()
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    delivered = models.BooleanField(default=True)

    # For shared order functionality
    shared_order = models.BooleanField(default=False)
    shared_with = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.order_id)


class OrdersIterator:
    # Initialize the iterator with a list of orders and set the index to 0.
    def __init__(self, orders):
        self.orders = orders
        self.index = 0

    # Make the iterator itself iterable.
    def __iter__(self):
        return self

    # Get the next order in the list.
    def __next__(self):
        if self.index < len(self.orders):
            result = self.orders[self.index]
            self.index += 1
            return result
        # Raise StopIteration when there are no more orders.
        raise StopIteration



