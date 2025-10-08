from django.db import models
from django.contrib.auth.models import User

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='patient_mappings')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # prevent duplicate assignments

    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.name}"

