from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

class People(models.Model):
    id=models.IntegerField(primary_key=True)
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNO = models.IntegerField(default=0)

    class Meta:
        abstract=True

class Doctor(People):
    Major = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    address= models.CharField(max_length=100)
    in_date= models.DateField()
    out_date= models.DateField()
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(People):
    bloodGroup =models.CharField(max_length=5)
    height=models.IntegerField(default=0)
    weight=models.IntegerField(default=0)
    hospital=models.ForeignKey(Hospital,null=True)
    treatments=models.ManyToManyField(Doctor,through='Treatment',related_name="treatments")
    reservations=models.ManyToManyField(Doctor,through='Reservation',related_name="reservations")

    def __str__(self):
        return self.name


class Treatment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    inscription = models.CharField(max_length=100)
    treatmentContent= models.CharField(max_length=100)
    treatment_Date=models.DateField()

    def __str__(self):
        return "%s %s" % (self.treat_Date, self.patient.name)


class Reservation(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    reservation_Date=models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.patient.name, self.doctor.name, self.reservation_Date)
