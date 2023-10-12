from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from .forms import UserRegistrationForm, RetailerRegistrationForm

class RegistrationTests(TestCase):
    def test_user_registration(self):
        user_data = {
            'first_name': 'Sruthi',
            'last_name': 'Baru',
            'email': 'sruthibaru@gmail.com',
            'phone_number': '1234567890',
            'password': '12dbh282%$',
            'gender': 'Female',
            'date_of_birth': '1989-04-03',
        }
        response = self.client.post(reverse('register_user'), user_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertTrue(CustomUser.objects.get().is_active)

    def test_retailer_registration(self):
        retailer_data = {
            'business_name': 'S.S Enterprises',
            'address': '329 Lindell Blvd, St Louis',
            'email': 'ssenterprises@gmail.com',
            'phone_number': '9876543210',
        }
        response = self.client.post(reverse('register_retailer'), retailer_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertTrue(CustomUser.objects.get().is_active)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_user_registration_form(self):
        form = UserRegistrationForm(data={
            'first_name': 'Mayuk',
            'last_name': 'Yadav',
            'email': 'mayukyadav31@gmail.com',
            'phone_number': '0987654321',
            'password': 's33*%34',
            'gender': 'Male',
            'date_of_birth': '1997-05-10',
        })
        self.assertTrue(form.is_valid())

    def test_retailer_registration_form(self):
        form = RetailerRegistrationForm(data={
            'business_name': 'Bada Business',
            'address': 'Grand Blvd, St Louis City',
            'email': 'badabusiness@gmail.com',
            'phone_number': '2163748718',
        })
        self.assertTrue(form.is_valid())
