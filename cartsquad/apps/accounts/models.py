from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import datetime as dt

class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password = None):
        if not email:
            raise ValueError("Email is required")
        if not date_of_birth:
            raise ValueError("Date of birth is required")
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    is_child = models.BooleanField(("Is Child"), default=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    date_of_birth = models.DateField(default=timezone.now)
    owned_cart_ids = models.JSONField(blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)

    #AbstractBaseUser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)

    #Retailer fields
    is_retailer = models.BooleanField(default=False)
    business_name = models.CharField(max_length=100, blank=False, null=True)
    retailer_address = models.TextField(blank=True, null=True)
    product_id = models.JSONField(blank=True, null=True)
    retailer_name = models.CharField(max_length=100, blank=False, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = AccountManager()


    def save(self, *args, **kwargs):
        if self.date_of_birth:
            age = dt.date.today().year - self.date_of_birth.year
            if age < 18:
                self.is_child = True
            else:
                self.is_child = False
        self.full_name  = self.first_name + ' ' + self.last_name
        self.username = self.first_name
        super(Account, self).save(*args, **kwargs)
   
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
