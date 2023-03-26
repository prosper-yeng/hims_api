from rest_framework import serializers

from person.models import Patient
from sponsor_patient.serializers  import SponsorPatientSerializer
from person.models import Patient


from daily_attendance.serializers import DailyAttendanceSerializer

from patient_service_charge.serializers import CombinedPatientServiceChargeSerializer,PatientServiceCharge,PatientServiceChargeSerializer

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




class ServicesProvidederializer(serializers.ModelSerializer):
    # patient_attendance = DailyAttendanceSerializer(many=True,read_only=True)
    patient=  PatientServiceChargeSerializer()


    class Meta:
        model = Patient
        fields =['patient']




