# from django.urls import path
from rest_framework import routers


# Local apps imports
from .views import TreatmentOutcomeViewSet



router = routers.DefaultRouter()
router.register("api/treatement-outcome", TreatmentOutcomeViewSet, "treatement_outcome")

urlpatterns = router.urls
