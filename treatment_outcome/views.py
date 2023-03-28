from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import TreatmentOutcomeeSerializer,TreatmentOutcome


class TreatmentOutcomeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TreatmentOutcome.objects.all()
    serializer_class = TreatmentOutcomeeSerializer
