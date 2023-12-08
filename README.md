

# CartSquad: Shop Together with Friends

<img width="649" alt="Screenshot 2023-10-13 150447" src="https://github.com/mouli86/cartsquad/assets/126706206/fb378225-0edf-44ec-915f-d1a8d2e3d899">

Welcome to CartSquad, your go-to platform for collaborative online shopping. CartSquad is currently being designed to make online shopping a fun and social experience by enabling users to shop together with friends or family members, no matter where they are.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [How It Works](#how-it-works)
- [Using Shared Carts](#using-shared-carts)

## Getting Started

### Installation

- Clone this repository to your local machine:
  ```shell
  git clone https://github.com/lmouli86/cartsquad.git
  ```

- Navigate to the project directory:
  ```shell
  cd cartsquad
  ```


- Configure your database settings and other environment variables.
- Make sure to update settings.py file with your desired DBMS
- Install the required packages by running the following command:
  ```shell
  pip install -r requirements.txt
  ```

- Run the database migrations:
  ```shell
  python manage.py migrate accounts
  python manage.py migrate products
  python manage.py migrate carts
  python manage.py migrate orders
  ```
- These migrations contain the models for the application and are dependent on each other. So, make sure to run them in the order specified above.

- Migrate the database:
  ```shell
  python manage.py makemigrations
  ```

- Run the development server:
  ```shell
  python manage.py runserver
  ```

- Access the CartSquad web application in your web browser at `http://127.0.0.1:8000`.

## Features

- **Create Shopping Carts:** Users can create virtual shopping carts and add products to them.

- **Invite Friends:** Invite friends to join your shopping cart, shop together, and collaborate on selecting items.

- **Real-Time Updates:** Get real-time updates on the cart's contents and see what your friends are adding.

- **Product Search:** Search for products using attributes like color, object type.

## How It Works

1. **Sign Up or Log In:** Register an account or log in to your existing CartSquad account.

2. **Create a Cart:** Start by creating a new shopping cart, name it, and add your desired products.

3. **Invite Friends:** Invite your friends to join your cart by add their CartSquad email address while creating a new shared cart or updating an existing shared cart.

4. **Shop Together:** Collaborate with your friends in real time. Everyone can add, remove, or comment on products.

5. **Check Out:** Once you're done, proceed to the checkout.

## Using Shared Carts

- **Create a Shared Cart:** To create a shared cart, From cart page click on the "View Shared Cart" button and Select New Shared Cart Button. In shared cart page, enter the email address of the person you want to share the cart with sperated by semicolon(;) with Shared Cart Name and Description and click on the "Create Shared Cart" button.

- **Update a Shared Cart:** To update a shared cart, From cart page click on the "View Shared Cart" button and Select Modify button next your shared carts and update the email address of the person you want to share the cart with sperated by semicolon(;) with Shared Cart Name and Description and click on the "Update" button.

- **Delete a Shared Cart:** To delete a shared cart, From cart page click on the "View Shared Cart" button and Select Delete button next your shared carts and click on the "Delete" button.

- **Join a Shared Cart:** To join a shared cart, from shared carts page,  select Accept button in Pending Shared Carts section.

- **Viewing a Shared Cart:** To view a shared cart, from shared carts page, select Shared Cart Name in Active Shared Carts section. For viewing a shared cart, you must accept the shared cart and be invited to that cart.

- **Checking Out a Shared Cart:** To checkout a shared cart, from cart summary page click on the "Checkout" button. For checking out a shared cart, you must be owner of the cart to do this.

