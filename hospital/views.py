from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreatePatientForm
from .forms import CreateDoctorForm
from django.db.models import Q
from django.shortcuts import render
from .models import *
# Create your views here.
from mysite.views import LoginRequireMixin
from django.utils import timezone


class DoctorView(TemplateView):
    template_name = 'hospital/Doctor.html'
    def get_context_data(self, **kwargs):
        context = super(DoctorView, self).get_context_data(**kwargs)
        context['objects_list'] = ['patient', 'Treatment', 'Reservation']
        return context

class PatientList(ListView) :
    template_name = 'hospital/Doctor/patient.html'
    def get_queryset(self):
        return Patient.objects.filter(treatment__doctor__user=self.request.user).all()

class TreatmentList(ListView) :
    template_name = 'hospital/Doctor/treatment.html'
    def get_queryset(self) :
        return Treatment.objects.filter(patient__treatment__doctor__user=self.request.user).all()

class ReservationList(ListView) :
    template_name = 'hospital/Doctor/reservation.html'
    def get_queryset(self) :
        return Reservation.objects.filter(patient__reservation__doctor__user=self.request.user).all()

class PatientDetail(DetailView) :
    template_name = 'hospital/Doctor/patient_detail.html'
    model = Patient

class TreatmentDetail(DetailView) :
    template_name = 'hospital/Doctor/treatment_detail.html'
    model = Treatment

class ReservationDetail(DetailView) :
    template_name = 'hospital/Doctor/reservation_detail.html'
    model = Reservation

class PatientupdateView(LoginRequireMixin, UpdateView):
    template_name = 'hospital/Doctor/patient_form.html'
    model = Patient
    fields = ['hospital']
    success_url = reverse_lazy('patient_list')

class TreatmentupdateView(LoginRequireMixin, UpdateView):
    template_name = 'hospital/Doctor/treatment_form.html'
    model = Treatment
    fields = ['inscription','treatmentContent','treatment_Date']
    success_url = reverse_lazy('treatment_list')

class ReservationupdateView(LoginRequireMixin, UpdateView):
    template_name = 'hospital/Doctor/reservation_form.html'
    model = Reservation
    fields = ['reservation_Date']
    success_url = reverse_lazy('reservation_list')

class Treatmentcreateview(LoginRequireMixin, CreateView): #환자 용
    template_name='hospital/Doctor/treatment_add.html'
    model = Treatment
    fields = ['patient','inscription','treatmentContent']
    success_url = reverse_lazy('treatment_list')
    def form_valid(self,form):
        form.instance.treatment_Date = timezone.now()
        form.instance.doctor =self.request.user.doctor
        return super(Treatmentcreateview, self).form_valid(form)

class reservationView(ListView): #환자 용
    template_name='hospital/Patient.html'

    def get_queryset(self):
        return Reservation.objects.filter(patient__user=self.request.user).all()

class reservDeleteView(DeleteView): #환자 용
    template_name='hospital/Patient/reservation_confirm_delete.html'
    model=Reservation
    success_url=reverse_lazy('hospital:index')

class PatientReservationupdateView(LoginRequireMixin, UpdateView): #환자 용
    template_name='hospital/Patient/reservation_update.html'
    model = Reservation
    fields = ['reservation_Date']
    success_url = reverse_lazy('reservation')

class reservationcreateview(LoginRequireMixin, CreateView): #환자 용
    template_name='hospital/Patient/reservation_add.html'
    model = Reservation
    fields = ['reservation_Date','doctor']
    success_url = reverse_lazy('reservation')
    def form_valid(self,form):
        form.instance.patient=self.request.user.patient
        return super(reservationcreateview, self).form_valid(form)


class IndexView(TemplateView):
    template_name = 'hospital/index.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateDoctorForm
    success_url = reverse_lazy('create_user_done')

class CreateUserPView(CreateView):
    template_name = 'registration/signupP.html'
    form_class =  CreatePatientForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
