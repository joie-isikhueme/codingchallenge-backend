from rest_framework import serializers
from HospitalApp.models import Users, Appointments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','FirstName','LastName','UserRole','Email')
    
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointments
        fields=('id','PatientName','DoctorName','DateOfAppointment','TimeOfAppointment')