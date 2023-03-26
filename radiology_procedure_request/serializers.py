from rest_framework import serializers
from .models import RadiologyProcedureRequest
from consultation_diagnosis.serializers import CombinedConsultedDiagnosedPatientSerializer


class RadiologyProcedureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyProcedureRequest
        # exclude = ["created_at", "updated_at"]
        fields = "__all__"
        read_only_fields = ["id"]


class RadiologyProcedureRequestListSerializer(serializers.ModelSerializer):
    consultation_diagnosis = CombinedConsultedDiagnosedPatientSerializer(many=False, read_only=True)
    consultation_diagnosis = CombinedConsultedDiagnosedPatientSerializer(many=False, read_only=True)
    created_by = serializers.CharField(read_only=True)
    created_by_id = serializers.CharField(read_only=True)
    radiology_procedure = serializers.CharField(read_only=True)
    radiology_procedure_id = serializers.CharField(read_only=True)
    sponsor = serializers.CharField(read_only=True)
    sponsor_id = serializers.CharField(read_only=True)
    class Meta:
        model = RadiologyProcedureRequest
        # exclude = ["created_at", "updated_at"]
        fields = "__all__"
        read_only_fields = ["id"]
