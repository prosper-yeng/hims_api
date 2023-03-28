

# Python/django imports
from rest_framework import serializers
from patient_discharge.models import PatientDischarge
from treatment_outcome.serializers import TreatmentOutcomeeSerializer

class PatientDischargeSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source="created_by.get_full_name",read_only=True)
    patient_name = serializers.CharField(source="patient.full_name",read_only=True)
    doctor_name = serializers.CharField(source="doctor.full_name",read_only=True)
    treatment_outcome =   TreatmentOutcomeeSerializer(source="patients_discharge",many=True,read_only=True)
    class Meta:
        model = PatientDischarge
        # exclude = []
        fields = ['patient','admission','doctor','reason','created_by_name','patient_name','doctor_name','created_at','updated_at','treatment_outcome']
        read_only_fields = ["id"]
