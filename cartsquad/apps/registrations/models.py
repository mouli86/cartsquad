from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    is_child = models.BooleanField(_("Is Child"), default=False)  # Field to indicate if the user is a child
    is_retailer = models.BooleanField(_("Is Retailer"), default=False)  # Field to indicate if the user is a retailer
    first_name = models.CharField(max_length=30)  # First name of the user
    last_name = models.CharField(max_length=30)  # Last name of the user
    email = models.EmailField(unique=True)  # User's unique email address
    phone_number = models.CharField(max_length=15)  # User's phone number
    password = models.CharField(max_length=128)  # User's password (hashed)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])  # User's gender
    date_of_birth = models.DateField()  # User's date of birth

    # Retailer-specific fields
    business_name = models.CharField(max_length=100, blank=True, null=True)  # Name of the business for retailers
    address = models.TextField(blank=True, null=True)  # Address of the business for retailers

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            age = (timezone.now().date() - self.date_of_birth).days // 365
            if age < 18:
                self.is_child = True  # If the user is under 18, set is_child to True
            else:
                self.is_child = False  # If the user is 18 or older, set is_child to False
        super(User, self).save(*args, **kwargs)
