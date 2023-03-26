from django.urls import path,include

# ALL REPORTS
urlpatterns = [
    path('', include('reports.general.urls')),
    path('', include('reports.claims.urls')),

]