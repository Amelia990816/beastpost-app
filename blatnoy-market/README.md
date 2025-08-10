# BLATNOY MARKET

BLATNOY MARKET is a multi-vendor marketplace web application built using Python and Django. This application allows multiple vendors to register, manage their products, and sell them to customers through a unified platform.

## Features

- **User Authentication**: Custom user model with registration, login, logout, password reset, and email verification.
- **Vendor Management**: Vendors can register, manage their stores, and list products.
- **Product Catalog**: Users can browse, search, and filter products by categories.
- **Shopping Cart**: Users can add products to their cart and proceed to checkout.
- **Order Management**: Users can view their order history and manage their orders.
- **Admin Dashboard**: Admins can manage users, vendors, and products.

## Project Structure

The project is structured into several apps for better organization:

- **accounts**: Handles user authentication and profiles.
- **marketplace**: Manages products, categories, and orders.
- **vendors**: Manages vendor registration and store functionalities.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blatnoy-market
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update the database settings in `config/settings.py`.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Admin panel can be accessed at `http://127.0.0.1:8000/admin/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.