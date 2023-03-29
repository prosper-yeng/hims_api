from rest_framework import serializers

from .models import Procedure,ProcedureType


class ProcedureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureType
        fields = "__all__"

        read_only_fields = ("id",)


class ProcedureSerializer(serializers.ModelSerializer):
    procedure_type = ProcedureTypeSerializer(read_only=True)
    procedure_type_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Procedure
        fields = [
            "id",
            "name",
            "procedure_type_id",
            "gdrg",
            "icd_code",
            "description",
            "status",
            "created_by",
            "procedure_type",
        ]
        # depth = 1

        read_only_fields = ("id",)

        


