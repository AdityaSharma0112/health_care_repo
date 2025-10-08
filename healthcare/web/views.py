from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


Patient = apps.get_model('patients', 'Patient')
Doctor = apps.get_model('doctors', 'Doctor')
PatientDoctorMapping = apps.get_model('mappings', 'PatientDoctorMapping')

def home(request):
    return render(request, 'web/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'web/login.html', {'form': form})

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'web/register.html', {'form': form})

def patients_list(request):
 
    patients = Patient.objects.all()
    return render(request, 'web/patients.html', {'patients': patients})

def doctors_list(request):
   
    doctors = Doctor.objects.all()
    return render(request, 'web/doctors.html', {'doctors': doctors})


def create_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        # You can add user assignment if needed
        Patient.objects.create(name=name, age=age, gender=gender, contact=contact)
        return render(request, 'web/patients.html', {'patients': Patient.objects.all(), 'message': 'Patient added successfully!'})
    return render(request, 'web/create_patient.html')


def create_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        Doctor.objects.create(name=name, specialization=specialization, contact=contact, email=email)
        return render(request, 'web/doctors.html', {'doctors': Doctor.objects.all(), 'message': 'Doctor added successfully!'})
    return render(request, 'web/create_doctor.html')

def create_mapping(request):
    return render(request, 'web/create_mapping.html')

def mappings_list(request):
    mappings = PatientDoctorMapping.objects.all()
    return render(request, 'web/mappings.html', {'mappings': mappings})

def delete_mapping(request, mapping_id):
    mapping = get_object_or_404(PatientDoctorMapping, id=mapping_id)
    mapping.delete()
    return HttpResponseRedirect(reverse('mappings-list'))

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        
        patient.name = name
        patient.age = age
        patient.gender = gender
        patient.contact = contact
        patient.save()
        
        return HttpResponseRedirect(reverse('patient-detail', args=[patient_id]))
    
    return render(request, 'web/patient_detail.html', {'patient': patient})

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()
    return HttpResponseRedirect(reverse('patients-list'))

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        
        doctor.name = name
        doctor.specialization = specialization
        doctor.contact = contact
        doctor.email = email
        doctor.save()
        
        return HttpResponseRedirect(reverse('doctor-detail', args=[doctor_id]))
    
    return render(request, 'web/doctor_detail.html', {'doctor': doctor})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctor.delete()
    return HttpResponseRedirect(reverse('doctors-list'))
