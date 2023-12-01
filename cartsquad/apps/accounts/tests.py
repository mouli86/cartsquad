# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal

class AccountAndAuthTests(TestCase):

    def test_customer_registration_and_login(self):
        # Simulate a customer registration
        response = self.client.post(reverse('customer_register'), {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'password1': 'securepassword123', 'password2': 'securepassword123', 'phone_number': '1234567890', 'gender': 'Male', 'date_of_birth': '1990-01-01'})
        self.assertEqual(response.status_code, 302)  # Check if the registration redirects to the homepage

        # Simulate customer login
        response_login = self.client.post(reverse('user_login'), {'email': 'john.doe@example.com', 'password': 'securepassword123'})
        self.assertEqual(response_login.status_code, 302)  # Check if the login redirects to the homepage
        self.assertContains(response_login, 'John Doe') 

    def test_retailer_registration_and_login(self):
        # Simulate a retailer registration
        response = self.client.post(reverse('retailer_register'), {'business_name': 'Tech Emporium', 'retailer_name': 'tech_shop', 'email': 'tech.shop@example.com', 'password1': 'securepassword456', 'password2': 'securepassword456', 'phone_number': '9876543210', 'retailer_address': '123 Tech Street', 'is_retailer': True})
        self.assertEqual(response.status_code, 302)  # Check if the registration redirects to the product view

        # Simulate retailer login
        response_login = self.client.post(reverse('retailer_login'), {'email': 'tech.shop@example.com', 'password': 'securepassword456'})
        self.assertEqual(response_login.status_code, 302)  # Check if the login redirects to the product view
        self.assertContains(response_login, 'Tech Emporium')  

    def test_authenticated_user_profile_view(self):
        # Simulate an authenticated user
        self.client.login(email='mouli.naidu@gmail.com', password='securepassword123')

        # Access the profile view
        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 200)  # Check if the profile view is accessible

        # Check if user details are present in the response
        self.assertContains(response, 'Mouli Naidu')
        self.assertContains(response, 'mouli.naidu@gmail.com')
        self.assertContains(response, 'Male')

    def test_user_logout(self):
        # Simulate an authenticated user
        self.client.login(email='mouli.naidu@gmail.com', password='securepassword123')

        # Simulate user logout
        response = self.client.get(reverse('logout_user'))
        self.assertEqual(response.status_code, 302)  # Check if the logout redirects to the homepage

        # Access a restricted view after logout
        response_restricted = self.client.get(reverse('profile_view'))
        self.assertEqual(response_restricted.status_code, 302)  # Check if attempting to access the profile view redirects to the login page

 
