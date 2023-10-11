from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    is_child = models.BooleanField(_("Is Child"), default=False)
    is_retailer = models.BooleanField(_("Is Retailer"), default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    date_of_birth = models.DateField()

    # Retailer-specific fields
    business_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            age = (timezone.now().date() - self.date_of_birth).days // 365
            if age < 18:
                self.is_child = True
            else:
                self.is_child = False
        super(User, self).save(*args, **kwargs)
