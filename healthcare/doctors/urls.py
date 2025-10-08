from django.urls import path
from .views import DoctorCreateView, DoctorListView, DoctorDetailView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor-list'),
    path('create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('<int:id>/', DoctorDetailView.as_view(), name='doctor-detail'),
]
