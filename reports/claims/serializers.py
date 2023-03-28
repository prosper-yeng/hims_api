from rest_framework import serializers

from person.models import Patient
from sponsor_patient.serializers  import SponsorPatientSerializer
from person.models import Patient


from daily_attendance.serializers import DailyAttendanceSerializer

from patient_service_charge.serializers import CombinedPatientServiceChargeSerializer
from patient_diagnosis.serializers import PatientDiagnosisDetailsSerializer
from diagnosis.serializers import DiagnosisDetailSerializer

from doctors_note.serializers import DoctorsNote,DoctorsNoteDetailsSerializer,DoctorsNoteSerializer
from patient_diagnosis.serializers import PatientDiagnosisDetailsSerializer,PatientDiagnosis
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"

class ClientInfomatonSerializer(serializers.ModelSerializer):

    
    date_of_birth = serializers.CharField(source='user.date_of_birth')
    gender= serializers.CharField(source="user.gender", read_only=True)
    national_id = serializers.CharField(source="user.national_id", read_only=False)
    first_name = serializers.CharField(source="user.first_name", read_only=False)
    last_name = serializers.CharField(source="user.last_name", read_only=False)
    middle_name =serializers.CharField(source="user.middle_name", read_only=False)
    patient_id = serializers.IntegerField(source='pk', read_only=False)

    patient_attendance = DailyAttendanceSerializer(many=True,read_only=True)

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

    first_name = serializers.CharField(source="user.first_name", read_only=False)
    last_name = serializers.CharField(source="user.last_name", read_only=False)
    middle_name =serializers.CharField(source="user.middle_name", read_only=False)
    services_provided=  CombinedPatientServiceChargeSerializer(many=True,read_only=True,source="patiant_service_charges")
    client_id = serializers.IntegerField(source='pk',help_text="id of the patient")
    num_of_visits = serializers.SerializerMethodField()

 

 
    class Meta:
        model = Patient
        fields =['client_id',
                 'full_name',
                 "first_name",
                 "last_name",
                 "middle_name"
,                "created_on",
                 "modified_on",
                 "num_of_visits",
                 'services_provided',
                  
                ]

    def get_num_of_visits(self, obj):
        return obj.patiant_service_charges.count()




class DiagnosesSerializer(serializers.ModelSerializer):

    diagnosis = PatientDiagnosisDetailsSerializer()
    
 
    class Meta:
        model = PatientDiagnosis
        fields =[
                "diagnosis",
                ]
        
 





