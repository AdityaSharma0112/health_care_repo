from django.urls import path
from .views import PatientCreateView, PatientListView, PatientDetailView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient-list'),
    path('create/', PatientCreateView.as_view(), name='patient-create'),
    path('<int:id>/', PatientDetailView.as_view(), name='patient-detail'),
]
