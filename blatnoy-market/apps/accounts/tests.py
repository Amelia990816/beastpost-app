# Tests for Accounts App
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(user.is_vendor)

    def test_create_vendor_user(self):
        user = User.objects.create_user(
            username='vendor',
            email='vendor@example.com',
            password='vendorpass123',
            is_vendor=True
        )
        self.assertTrue(user.is_vendor)