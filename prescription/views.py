# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PrescriptionSerializer, CombinedDiagnosisPrescriptionSerializer
from .models import Prescription


class PrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class CombinedDiagnosisPrescriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Prescription.objects.all()
        serialized = CombinedDiagnosisPrescriptionSerializer(query_data, many=True)
        return Response(serialized.data)
