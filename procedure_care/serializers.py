from rest_framework import serializers
from .models import ProcedureCare


# from procedure.serializers import ProcedureSerializer,Procedure,ProcedureType


class ProcedureCareSerializer(serializers.ModelSerializer):
    # procedures = ProcedureSerializer(source="procedure",read_only=True)
    
    class Meta:
        model = ProcedureCare
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
