from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from person.serializers import Patient

from .serializers import (ClientInfomatonSerializer, PatientDiagnosis,
                          PatientDiagnosisDetailsSerializer,
                          ProceduresSerializer, ServicesProvidedSerializer)
from procedure_care.models import Procedure
from procedure_care.serializers import ProcedureCare

# from rest_framework.views import APIView




# from doctors_note.serializers import DoctorsNote,DoctorsNoteDetailsSerializer


class CliantInfomationViewSet(generics.ListAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = ClientInfomatonSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Patient.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(
                created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class ServicesProvidedViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServicesProvidedSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Patient.objects.all().order_by('id')

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(
                created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class DiagnosesViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientDiagnosisDetailsSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = PatientDiagnosis.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(
                created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)



class ProcedureViewSet(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProceduresSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = ProcedureCare.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(
                created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)
