# Tests for Marketplace App
from django.test import TestCase
from django.contrib.auth import get_user_model
from vendors.models import Vendor
from marketplace.models import Category, Product

User = get_user_model()

class ProductCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='vendor',
            email='vendor@example.com',
            password='vendorpass123',
            is_vendor=True
        )
        self.vendor = Vendor.objects.create(
            user=self.user,
            store_name='Test Store'
        )
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )

    def test_create_product(self):
        product = Product.objects.create(
            vendor=self.vendor,
            category=self.category,
            title='Test Product',
            description='Test Description',
            price=99.99,
            stock=10
        )
        self.assertEqual(product.title, 'Test Product')
        self.assertEqual(product.price, 99.99)