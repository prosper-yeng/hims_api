# Python/django imports
from rest_framework import serializers

# Local app imports
from .models import DoctorsNote
from person.serializers import PatientSerializer


class DoctorsNoteSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(read_only=True,source='doctor.get_full_name')

    class Meta:
        model = DoctorsNote
        # exclude = ["created_at", "updated_at"]
        fields = ['patient','admission','note','doctor','doctor_name','treatment_plan','created_at','updated_at']

        read_only_fields = ["id"]


class DoctorsNoteDetailsSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(read_only=True,source='doctor.get_full_name')
    patient = PatientSerializer()

    class Meta:
        model = DoctorsNote
        # exclude = ["created_at", "updated_at"]
        fields = ['patient','admission','note','doctor','doctor_name','treatment_plan','created_at','updated_at']
        read_only_fields = ["id"]
