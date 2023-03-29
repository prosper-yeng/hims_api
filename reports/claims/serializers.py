from rest_framework import serializers

from daily_attendance.serializers import DailyAttendanceSerializer

from patient_diagnosis.serializers import (PatientDiagnosis,
                                           PatientDiagnosisDetailsSerializer)
from patient_discharge.serializers import PatientDischargeSerializer
from patient_service_charge.serializers import \
    CombinedPatientServiceChargeSerializer
from person.models import Patient
from procedure.serializers import  ProcedureSerializer
from procedure_care.serializers import ProcedureCare
from sponsor_patient.serializers import SponsorPatientSerializer


class AbstractPatientNameSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.CharField(source='user.date_of_birth')
    gender = serializers.CharField(source="user.gender", read_only=True)
    national_id = serializers.CharField(
        source="user.national_id", read_only=False)
    first_name = serializers.CharField(
        source="user.first_name", read_only=False)
    last_name = serializers.CharField(source="user.last_name", read_only=False)
    middle_name = serializers.CharField(
        source="user.middle_name", read_only=False)
    email = serializers.CharField(source="user.email")
    email = serializers.CharField(source="user.email")
    client_id = serializers.IntegerField(
        source="user.id", help_text='Patient ID')

    class Meta:
        model = Patient
        fields = (
            "client_id",
            "title",
            "first_name",
            "last_name",
            "middle_name",
            "email",
            'hospital_record_no',
            'age',
            "full_name",
            "title",
            "date_of_birth",
            "gender",
            "national_id",

        )


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"


class ClientInfomatonSerializer(serializers.ModelSerializer):

    date_of_birth = serializers.CharField(source='user.date_of_birth')
    gender = serializers.CharField(source="user.gender", read_only=True)
    national_id = serializers.CharField(
        source="user.national_id", read_only=False)
    first_name = serializers.CharField(
        source="user.first_name", read_only=False)
    last_name = serializers.CharField(source="user.last_name", read_only=False)
    middle_name = serializers.CharField(
        source="user.middle_name", read_only=False)
    patient_id = serializers.IntegerField(source='pk', read_only=False)

    patient_attendance = DailyAttendanceSerializer(many=True, read_only=True)

    patient_sponsor = SponsorPatientSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = (
            "patient_id",
            "title",
            "first_name",
            "last_name",
            "middle_name",
            'hospital_record_no',
            'age',
            "full_name",
            "title",
            "date_of_birth",
            "gender",
            "national_id",
            "created_on",
            "modified_on",
            "patient_attendance",
            "patient_sponsor",

        )


class ServicesProvidedSerializer(serializers.ModelSerializer):
    # patient_attendance = DailyAttendanceSerializer(many=True,read_only=True)

    first_name = serializers.CharField(
        source="user.first_name", read_only=False)
    last_name = serializers.CharField(source="user.last_name", read_only=False)
    middle_name = serializers.CharField(
        source="user.middle_name", read_only=False)
    services_provided = CombinedPatientServiceChargeSerializer(
        many=True, read_only=True, source="patiant_service_charges")
    client_id = serializers.IntegerField(
        source='pk', help_text="id of the patient")
    num_of_visits = serializers.SerializerMethodField()
    # treatment_outcome =  TreatmentOutcomeeSerializer(many=True,read_only=True,source="patient_discharge_patient")
    patient_discharge_patient = PatientDischargeSerializer(
        many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['client_id',
                  'full_name',
                  "first_name",
                  "last_name",
                  "middle_name",                "created_on",
                  "modified_on",
                  "num_of_visits",
                  'services_provided',
                  #  "treatment_outcome",
                  "patient_discharge_patient",

                  ]

    def get_num_of_visits(self, obj):
        return obj.patiant_service_charges.count()


class DiagnosesSerializer(serializers.ModelSerializer):

    diagnosis = PatientDiagnosisDetailsSerializer()

    class Meta:
        model = PatientDiagnosis
        fields = [
            "diagnosis",
        ]


class ProceduresSerializer(serializers.ModelSerializer):

    procedure = ProcedureSerializer()
    patient = AbstractPatientNameSerializer()
    # procedure_care_patient = ProcedureCareSerializer(many=True)

    class Meta:
        model = ProcedureCare
        fields = "__all__"
        # depth =1
