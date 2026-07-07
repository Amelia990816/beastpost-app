# Blatnoy Market

A full-featured Django-based multi-vendor marketplace application.

## Features

- **User Authentication**: Registration, login, profile management
- **Vendor Management**: Vendor registration, store setup, product management
- **Product Catalog**: Browse, search, and filter products by categories
- **Shopping Cart**: Add products to cart and checkout
- **Order Management**: View order history, track orders
- **Admin Dashboard**: Comprehensive admin panel for managing users, vendors, and orders
- **REST API**: Full REST API for frontend integration
- **Stripe Integration**: Payment processing ready

## Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (development), PostgreSQL (production)
- **API**: Django REST Framework
- **Authentication**: Django Built-in + django-allauth (optional)
- **Payments**: Stripe
- **CORS**: django-cors-headers

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blatnoy-market
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create migrations and migrate:
   ```bash
   python manage.py makemigrations
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

## API Endpoints

### Accounts
- `POST /api/accounts/register/` - User registration
- `GET /api/accounts/profile/` - Get user profile

### Vendors
- `GET /api/vendors/dashboard/` - Get vendor dashboard
- `POST /api/vendors/create/` - Create vendor profile

### Marketplace
- `GET /api/marketplace/products/` - List all products
- `POST /api/marketplace/orders/create/` - Create order

## Admin Dashboard

Access the admin panel at `http://127.0.0.1:8000/admin/`

### Features:
- **User Management**: Manage users, profiles, and vendor status
- **Vendor Management**: Approve/manage vendor stores
- **Product Management**: Add, edit, and manage products
- **Order Management**: View and manage customer orders with inline editing
- **Category Management**: Organize products into categories

## Environment Variables

Create a `.env` file in the `blatnoy-market` directory:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
STRIPE_PUBLIC_KEY=your-stripe-public-key
STRIPE_SECRET_KEY=your-stripe-secret-key
```

## Project Structure

```
blatnoy-market/
├── apps/
│   ├── accounts/          # User authentication & profiles
│   ├── marketplace/       # Products, categories, orders
│   └── vendors/          # Vendor management
├── config/               # Django configuration
├── templates/            # HTML templates
├── static/              # CSS, JavaScript, images
├── manage.py
├── requirements.txt
└── README.md
```

## License

MIT License - see LICENSE file for details
