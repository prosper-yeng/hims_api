from rest_framework import serializers

from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source="created_by.get_full_name")
    class Meta:
        model = Status
        fields = ["id", "name", "created_by","created_by_name"]
