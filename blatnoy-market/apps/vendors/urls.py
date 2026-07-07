from django.urls import path
from .views import VendorDashboardView, CreateVendorView

urlpatterns = [
    path('dashboard/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('create/', CreateVendorView.as_view(), name='create_vendor'),
]