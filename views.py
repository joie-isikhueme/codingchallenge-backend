from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from HospitalApp.models import Users, Appointments
from HospitalApp.serializers import UserSerializer, AppointmentSerializer
# Create your views here.

@csrf_exempt
def userApi(request,id=0):
    if request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Sucessfully!", safe=False)
#    elif request.method=='GET':
#       users=Users.objects.all()
#       user_serializer=UserSerializer(users,many=True)
#       return JsonResponse(user_serializer.data, safe=False) 
    
    elif request.method=='DELETE':
        
        user=Users.objects.get(id=id)
        user.delete()
        return JsonResponse("User Account Deleted",safe=False)

@csrf_exempt
def appointmentApi(request, id=0):
    if request.method=='POST':
        appointment_data=JSONParser().parse(request)
        appointment_serializer=AppointmentSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse("You have sucessfully made an appointment!", safe=False)
#    elif request.method=='GET':
#        appointments=Appointments.objects.all()
#        appointment_serializer=AppointmentSerializer(appointments, many=True)
#        return JsonResponse(appointment_serializer.data, safe=False)
    

    elif request.method=="DELETE":
        appointment=Appointments.objects.get(id=id)
        appointment.delete()
        return JsonResponse("Appointment Deleted",safe=False)
