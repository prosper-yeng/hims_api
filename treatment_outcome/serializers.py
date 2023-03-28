# Python/django imports
from rest_framework import serializers

# from patient_discharge.serializers import PatientDischargeSerializer

from .models import TreatmentOutcome


class TreatmentOutcomeeSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source="patient_discharge.patient.full_name", read_only=True)
    patient_id = serializers.IntegerField(source="patient_discharge.patient.pk", read_only=True)

    created_by_name = serializers.CharField(source="created_by.get_full_name", read_only=True)
    doctor_responsible = serializers.CharField(source="patient_discharge.doctor.full_name", read_only=True)

    # patient_discharge = PatientDischargeSerializer(read_only=True)

    class Meta:
        model = TreatmentOutcome
        # fields = "__all__"

        fields = ['discharged', 'died', 'cout',
                  'absconded', 'created_by_name',
                  'doctor_responsible',
                  'patient_name', 'patient_id',
                  'created_at', 'updated_at','patient_discharge',
                  ]
        read_only_fields = ["id"]
