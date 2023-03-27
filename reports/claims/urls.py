from django.urls import path
from . import views


# CLAIMS REPORT
urlpatterns = [
    path('api/reports/client-infomation/',views.CliantInfomationViewSet.as_view(),name="client_infomation"),
    path('api/reports/services-provided/',views.ServicesProvidedViewSet.as_view(),name="services_provided"),
    path('api/reports/diagnoses/',views.DiagnosesViewSet.as_view(),name="diagnoses"),
]

