from django.db import models
import datetime as dt
import uuid

class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    user_id = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, db_column='user_id')
    products = models.JSONField(null=True, blank=True)
    order_total = models.DecimalField(decimal_places=2, max_digits=10)
    order_date_created = models.DateField()
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    delivered = models.BooleanField(default=True)

    #For shared order functionality
    shared_order = models.BooleanField(default=False)
    shared_with = models.JSONField(null=True, blank=True)

    # String representation of the Orders instance.
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



