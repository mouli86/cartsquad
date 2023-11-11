from django.db import models
import datetime as dt

# Create your models here.
class Cart(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    product_id =models.IntegerField()
    user_id =  models.IntegerField()
    quantity = models.IntegerField()
    is_billed = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['product_id','user_id', 'quantity']

    def __str__(self):
        return self.product_id, self.user_id
    
    # This function will be called when a new product is added to the Cart.
    def save(self, *args, **kwargs):
        self.product_date_modified = dt.date.today()
        self.product_date_added = dt.date.today()
        self.product_status = True
        super(Cart, self).save(*args, **kwargs)

    def atc(self, product_id, user_id, quantity):
        self.product_id = product_id
        self.user_id = user_id
        self.quantity = quantity
        # super(Cart, self).save()
        self.save()