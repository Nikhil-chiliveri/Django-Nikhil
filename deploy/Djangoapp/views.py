from django.shortcuts import render
from django.http import JsonResponse
from .models import CourseRegistration
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Student_register(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            CourseRegistration.objects.create(name=data["name"],email=data["email"],course=data["course"],phone=data["phone"])
            return JsonResponse({"status":"sucess","message":"Registration successful"})
        return JsonResponse({"status":"failure","message":"only post method allowed"}) 

    except Exception as E:
        return JsonResponse({"message":"something went wrong"})
    
def Course_details(request):
    try:
        if request.method=="GET":
            result=list( CourseRegistration.objects.values())
            if len(result)==0:
                msg="NO records found"
            else:
                msg="Data retriewed sucessfully"
                return JsonResponse({"status":"sucess","message":msg,"registrations":result})

    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
