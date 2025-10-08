from django.urls import path
from .views import home, patients_list, doctors_list, create_patient, create_doctor, login_view, register_view, create_mapping, mappings_list, delete_mapping, patient_detail, delete_patient, doctor_detail, delete_doctor

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('patients/', patients_list, name='patients-list'),
    path('doctors/', doctors_list, name='doctors-list'),
    path('mappings/', mappings_list, name='mappings-list'),
    path('patients/create/', create_patient, name='create-patient'),
    path('doctors/create/', create_doctor, name='create-doctor'),
    path('mappings/create/', create_mapping, name='create-mapping'),
    path('mappings/delete/<int:mapping_id>/', delete_mapping, name='delete-mapping'),
    path('patients/<int:patient_id>/', patient_detail, name='patient-detail'),
    path('patients/delete/<int:patient_id>/', delete_patient, name='delete-patient'),
    path('doctors/<int:doctor_id>/', doctor_detail, name='doctor-detail'),
    path('doctors/delete/<int:doctor_id>/', delete_doctor, name='delete-doctor'),
]

