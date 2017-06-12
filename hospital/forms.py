from django import forms
import unicodedata
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from .models import Doctor, Patient
from django.conf import settings


class CreateDoctorForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phoneNO = forms.IntegerField()
    Major = forms.CharField()
    name= forms.CharField()
    class Meta:

        model = Doctor
        fields = ( "phoneNO", "Major", "name")
        model = User
        fields += ("username","email")

    def save(self, commit=True):
        user = super(CreateDoctorForm, self).save(commit=False)
        email = self.cleaned_data["email"]
        name=self.cleaned_data["name"]
        phoneNO = self.cleaned_data["phoneNO"]
        Major = self.cleaned_data["Major"]

        if commit:
            user.save()

            Doctor.objects.create(
                user=user,
                email=email,
                phoneNO=phoneNO,
                Major=Major,
                name=name
                )

        return user



class CreatePatientForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phoneNO = forms.IntegerField()
    bloodGroup = forms.CharField()
    height = forms.IntegerField()
    weight = forms.IntegerField()
    name= forms.CharField()
    class Meta:

        model = Patient
        fields = ("phoneNO", "bloodGroup", "height", "weight")
        model = User
        fields += ("username", "email")
    def save(self, commit=True):
        user = super(CreatePatientForm, self).save(commit=False)
        email = self.cleaned_data["email"]
        phoneNO = self.cleaned_data["phoneNO"]
        bloodGroup = self.cleaned_data["bloodGroup"]
        height = self.cleaned_data["height"]
        weight = self.cleaned_data["weight"]
        name = self.cleaned_data["name"]

        if commit:
            user.save()
            Patient.objects.create(
                user=user,
                email=email,
                bloodGroup=bloodGroup,
                height=height,
                weight=weight,
                name=name
            )
        return user
