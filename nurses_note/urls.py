# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import NursesNoteViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/nurses_note", NursesNoteViewSet, "nurses_note")

urlpatterns = router.urls
