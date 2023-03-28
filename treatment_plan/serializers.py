from rest_framework import serializers
from .models import TreatmentPlan
from person.serializers import PatientSerializer


class TreatmentPlanSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source="doctor")
    patient_condition_name = serializers.CharField(source="patient_condition")
    admission_name = serializers.CharField(source="admission")
    class Meta:
        model = TreatmentPlan
        # exclude = ["created_at", "updated_at"]
        fields = "__all__"
        read_only_fields = ["id","doctor_name","patient_condition_name","admission_name"]


class TreatmentPlanDetailsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor_name = serializers.CharField(source="doctor")
    patient_condition_name = serializers.CharField(source="patient_condition")

    class Meta:
        model = TreatmentPlan
        # exclude = ["created_at", "updated_at"]
        fields = "__all__"
        read_only_fields = ["id","doctor_name","patient_condition_name","admission_name"]
