"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hospital import views as hospital_views

urlpatterns = [
    #환자용
    url(r'^hospital/Patient/$', hospital_views.reservationView.as_view(),
    name = 'reservation' ),
    url(r'^hospital/Patient/(?P<pk>\d+)/delete/$', hospital_views.reservDeleteView.as_view(),
    name = 'reservdelete' ),
    url(r'^hospital/Patient/(?P<pk>\d+)/update/$',
    hospital_views.PatientReservationupdateView.as_view(), name = 'Patientreservationupdate' ),
    url(r'^hospital/Patient/add/$',
    hospital_views.reservationcreateview.as_view(), name = 'reservationadd' ),

    #의사용
    url(r'^hospital/Doctor/$', hospital_views.DoctorView.as_view(),
    name = 'Dview' ),
    url(r'^hospital/Doctor/patient/$', hospital_views.PatientList.as_view(),
    name = 'patient_list' ),
    url(r'^hospital/Doctor/treatment/$', hospital_views.TreatmentList.as_view(),
    name = 'treatment_list' ),
    url(r'^hospital/Doctor/reservation/$', hospital_views.ReservationList.as_view(),
    name = 'reservation_list' ),
    url(r'^hospital/Doctor/patient/(?P<pk>\d+)/$', hospital_views.PatientDetail.as_view(),
    name = 'patient_detail' ),
    url(r'^hospital/Doctor/treatment/(?P<pk>\d+)/$', hospital_views.TreatmentDetail.as_view(),
    name = 'treatment_detail' ),
    url(r'^hospital/Doctor/reservation/(?P<pk>\d+)/$', hospital_views.ReservationDetail.as_view(),
    name = 'reservation_detail' ),
    url(r'^hospital/Doctor/add/$',
    hospital_views.Treatmentcreateview.as_view(), name = 'treatmentadd' ),
    url(r'^hospital/Doctor/patient/(?P<pk>\d+)/update/$', hospital_views.PatientupdateView.as_view(),
    name = 'patientupdate' ),
    url(r'^hospital/Doctor/treatment/(?P<pk>\d+)/update/$', hospital_views.TreatmentupdateView.as_view(),
    name = 'treatmentupdate' ),
    url(r'^hospital/Doctor/reservation/(?P<pk>\d+)/update/$',
    hospital_views.ReservationupdateView.as_view(), name = 'reservationupdate' ),

    url(r'^admin/', admin.site.urls),
    url(r'^$', hospital_views.IndexView.as_view(), name = "root"),
    url(r'^hospital/', include('hospital.urls') ),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', hospital_views.CreateUserView.as_view(),
     name = 'signup'),
    url(r'^accounts/signupP/$', hospital_views.CreateUserPView.as_view(),
    name = 'signupP'),
    url(r'^accounts/signup/done$', hospital_views.RegisteredView.as_view(),
    name = 'create_user_done'),
]
