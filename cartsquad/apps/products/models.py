from django.db import models
import datetime as dt

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_description = models.TextField()
    product_image = models.ImageField()
    product_category = models.CharField(max_length=50)
    product_stock = models.IntegerField()
    product_rating = models.IntegerField()
    product_reviews = models.JSONField()
    product_brand = models.CharField(max_length=50)
    product_date_added = models.DateField()
    product_date_modified = models.DateField()
    product_status = models.BooleanField()
    product_discount = models.IntegerField()
    product_discount_price = models.IntegerField()
    # This field will have attributes of the product like color, size, etc. based on the product category.
    product_attributes = models.JSONField()
    product_search_terms = models.CharField(max_length=500)

    #to keep track of the retailer who added the product
    product_retailer_id = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE)

    
    REQUIRED_FIELDS = ['product_name', 'product_price', 'product_description',
                       'product_category', 'product_stock', 'product_brand', 'product_retailer_id']


    def __str__(self):
        return self.product_name
    
    # This function will be called when a new product is added to the database.
    def save(self, *args, **kwargs):
        self.product_date_modified = dt.date.today()
        self.product_date_added = dt.date.today()
        self.product_status = True
        self.product_search_terms = self.product_name.lower()
        super(Product, self).save(*args, **kwargs)

    def add_product(self, product_name, product_price, product_description, product_image, product_category, product_stock, product_rating, product_brand, product_retailer_id, product_search_terms):
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image
        self.product_category = product_category
        self.product_stock = product_stock
        self.product_rating = product_rating
        self.product_brand = product_brand
        self.product_retailer_id = product_retailer_id
        self.product_search_terms = self.product_name + product_search_terms
        self.save()
    
    def update_product(self, product_name, product_price, product_description, product_image, product_category, product_stock, product_rating, product_brand, product_retailer_id, product_search_terms):   
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image
        self.product_category = product_category
        self.product_stock = product_stock
        self.product_rating = product_rating
        self.product_brand = product_brand
        self.product_retailer_id = product_retailer_id
        self.product_search_terms = self.product_name + product_search_terms
        self.product_date_modified = dt.date.today()
        self.save()
