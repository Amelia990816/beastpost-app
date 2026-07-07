# Tests for Vendors App
from django.test import TestCase
from django.contrib.auth import get_user_model
from vendors.models import Vendor

User = get_user_model()

class VendorCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testvendor',
            email='testvendor@example.com',
            password='testpass123',
            is_vendor=True
        )

    def test_create_vendor(self):
        vendor = Vendor.objects.create(
            user=self.user,
            store_name='My Store',
            description='A test store'
        )
        self.assertEqual(vendor.store_name, 'My Store')
        self.assertTrue(vendor.is_active)