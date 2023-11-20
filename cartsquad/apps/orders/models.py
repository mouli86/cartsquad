from django.db import models
import datetime as dt

class Orders(models.Model):
    # Primary key for the Orders model, automatically generated as a large integer.
    seq_id = models.BigAutoField(primary_key=True)

    # Fields representing attributes of an order.
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    per_item_cost = models.DecimalField(decimal_places=2, max_digits=10)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)

    # Fields that are required for creating an order.
    REQUIRED_FIELDS = ['order_id', 'user_id', 'quantity', 'product_id', 'total_cost', 'per_item_cost']

    # String representation of the Orders instance.
    def __str__(self):
        return f"{self.product_id}, {self.user_id}, {self.order_id}"

    # Override the save method to set additional fields before saving.
    def save(self, *args, **kwargs):
        today = dt.date.today()
        self.product_date_modified = today
        self.product_date_added = today
        self.product_status = True
        super().save(*args, **kwargs)

    # Method to add orders with specified attributes.
    def add_orders(self, order_id, user_id, product_id, quantity, per_item_cost, total_cost):
        self.order_id = order_id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.per_item_cost = per_item_cost
        self.total_cost = total_cost
        self.save()
        

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
