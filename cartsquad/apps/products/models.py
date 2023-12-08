from django.db import models
import datetime as dt

# Create your models here.
class Product(models.Model):
    """
    Represents a product.
    Attributes:
        product_id (int): The unique identifier for the product.
        product_name (str): The name of the product.
        product_price (Decimal): The price of the product.
        product_description (str): The description of the product.
        product_image (ImageField): The image of the product.
        product_category (str): The category of the product.
        product_stock (int): The stock quantity of the product.
        product_rating (int, optional): The rating of the product (nullable).
        product_reviews (JSONField, optional): The reviews of the product (nullable).
        product_brand (str): The brand of the product.
        product_date_added (DateField): The date when the product was added.
        product_date_modified (DateField): The date when the product was last modified.
        product_status (bool): The status of the product.
        product_discount (int, optional): The discount percentage of the product (nullable).
        product_discount_price (int, optional): The discounted price of the product (nullable).
        product_attributes (JSONField, optional): The attributes of the product (nullable).
        product_search_terms (str): The search terms associated with the product.
        product_retailer_id (ForeignKey): The retailer who added the product.

    Methods:
        save(*args, **kwargs): Overrides the save method to update the modified date and search terms.
        add_product(product_name, product_price, product_description, product_image, product_category, product_stock, product_brand, product_retailer_id, product_search_terms, product_discount=0, product_discount_price=0): Adds a new product to the database.
        update_product(product_name, product_price, product_description, product_image, product_category, product_stock, product_brand, product_retailer_id, product_search_terms): Updates an existing product in the database.
    """

    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    product_category = models.CharField(max_length=50)
    product_stock = models.IntegerField()
    product_rating = models.IntegerField(null=True, blank=True)
    product_reviews = models.JSONField(null=True, blank=True)
    product_brand = models.CharField(max_length=50)
    product_date_added = models.DateField()
    product_date_modified = models.DateField()
    product_status = models.BooleanField()
    product_discount = models.IntegerField(blank=True, null=True)
    product_discount_price = models.IntegerField(blank=True, null=True)
    product_attributes = models.JSONField(null=True, blank=True)
    product_search_terms = models.CharField(max_length=500)
    product_retailer_id = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['product_name', 'product_price', 'product_description',
                       'product_category', 'product_stock', 'product_brand', 'product_retailer_id']

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.product_date_modified = dt.date.today()
        self.product_date_added = dt.date.today()
        self.product_status = True
        self.product_search_terms = self.product_name.lower()
        super(Product, self).save(*args, **kwargs)

    def add_product(self, product_name, product_price, product_description, product_image, product_category, product_stock, product_brand, product_retailer_id, product_search_terms, product_discount=0, product_discount_price=0):
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image
        self.product_category = product_category
        self.product_stock = product_stock
        self.product_brand = product_brand
        self.product_retailer_id = product_retailer_id
        self.product_search_terms = self.product_name + product_search_terms
        self.save()

    def update_product(self, product_name, product_price, product_description, product_image, product_category, product_stock, product_brand, product_retailer_id, product_search_terms):
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image
        self.product_category = product_category
        self.product_stock = product_stock
        self.product_brand = product_brand
        self.product_retailer_id = product_retailer_id
        self.product_search_terms = self.product_name + product_search_terms
        self.product_date_modified = dt.date.today()
        self.save()
