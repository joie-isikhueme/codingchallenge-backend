from django.conf.urls import url
from HospitalApp import views
from django.urls import path


urlpatterns=[
    #path('users/',views.ShowAll,),
    url(r'^user$',views.userApi),
    url(r'^user/([0-9])+', views.userApi),

    url(r'^appointment$',views.appointmentApi),
    url(r'^appointment/([0-9])+',views.appointmentApi)
   
]