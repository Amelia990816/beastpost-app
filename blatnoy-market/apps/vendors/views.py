from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Vendor

class VendorDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            vendor = request.user.vendor_profile
            return Response({
                "store_name": vendor.store_name,
                "description": vendor.description,
                "is_active": vendor.is_active,
                "created_at": vendor.created_at
            })
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor profile not found"}, status=status.HTTP_404_NOT_FOUND)

class CreateVendorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if hasattr(request.user, 'vendor_profile'):
            return Response({"error": "Vendor profile already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        try:
            vendor = Vendor.objects.create(
                user=request.user,
                store_name=data['store_name'],
                description=data.get('description', '')
            )
            request.user.is_vendor = True
            request.user.save()
            return Response({"message": "Vendor profile created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)