from django.db import models
import datetime as dt

# Create your models here.
class Orders(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    order_id =models.IntegerField()
    user_id =  models.IntegerField()
    product_id =  models.IntegerField()
    quantity = models.IntegerField()
    per_item_cost = models.DecimalField(decimal_places=2, max_digits=10)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)
    
    REQUIRED_FIELDS = ['order_id','user_id', 'quantity', 'product_id', 'total_cost', 'per_item_cost']

    def __str__(self):
        return self.product_id, self.user_id, self.order_id
    
    # This function will be called when a new product is added to the Cart.
    def save(self, *args, **kwargs):
        self.product_date_modified = dt.date.today()
        self.product_date_added = dt.date.today()
        self.product_status = True
        super(Orders, self).save(*args, **kwargs)

    def add_orders(self, order_id, user_id, product_id, quantity, per_item_cost ,total_cost):
        self.order_id = order_id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.per_item_cost = per_item_cost
        self.total_cost = total_cost
        self.save()