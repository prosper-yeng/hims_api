from django.urls import path
from rest_framework import routers
from .views import ProcedureViewSet,ProcedureTypeViewSet

router = routers.DefaultRouter()
router.register("api/procedure-type", ProcedureTypeViewSet, "procedure_type")


# router = routers.DefaultRouter()
router.register("api/procedure", ProcedureViewSet, "procedure")

urlpatterns = router.urls
