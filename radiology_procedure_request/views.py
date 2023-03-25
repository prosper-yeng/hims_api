from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyProcedureRequest
from .serializers import RadiologyProcedureRequestSerializer,RadiologyProcedureRequestListSerializer


class RadiologyProcedureRequestViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedureRequest.objects.all()
    serializer_class = RadiologyProcedureRequestSerializer



class RadiologyProcedureRequesListtViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedureRequest.objects.all()
    serializer_class = RadiologyProcedureRequestListSerializer
