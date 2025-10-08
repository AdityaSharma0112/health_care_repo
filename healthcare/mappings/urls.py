from django.urls import path
from .views import MappingCreateView, MappingListView, PatientMappingDetailView, MappingDeleteView

urlpatterns = [
    path('', MappingListView.as_view(), name='mapping-list'),
    path('create/', MappingCreateView.as_view(), name='mapping-create'),
    path('<int:patient_id>/', PatientMappingDetailView.as_view(), name='mapping-patient-detail'),
    path('delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
