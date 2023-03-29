# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ProcedureSerializer,ProcedureTypeSerializer
from .models import Procedure,ProcedureType




class ProcedureTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProcedureType.objects.all()
    serializer_class = ProcedureTypeSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
