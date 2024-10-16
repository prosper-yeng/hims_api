# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyProcedureRequestViewSet,RadiologyProcedureRequesListtViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_procedure_request",
    RadiologyProcedureRequestViewSet,
    "radiology_procedure_request",
)



router.register(
    "api/radiology_procedure_request_list",
    RadiologyProcedureRequesListtViewSet,
    "radiology_procedure_request_list",
)

urlpatterns = router.urls
