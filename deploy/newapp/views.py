from django.shortcuts import render
from django.http import JsonResponse
from .models import OrderDetails, MovieBooking,Book
import json
from django.views.decorators.csrf import  csrf_exempt

# Create your views here.


def GetOrders(request):
    try:
        if request.method=="GET":
            result=list(OrderDetails.objects.values())
            print(result)
            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved sucessfully"

            return JsonResponse({"status":"sucess","message":msg,"data":result,"total no of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})

    except Exception as e:
        return JsonResponse({"message":"something went wrong"})


def BookingDetails(request):
    try:
        if request.method=="GET":
            result=list(MovieBooking.objects.values())
            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved sucessfully"

            return JsonResponse({"status":"sucess","message":msg,"data":result,"total no of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
    

def BookDetails(request):
    try:
        if request.method=="GET":
            result=list(Book.objects.values())
            if len(result)==0:
                msg="No records found"
            else:
                msg="Data retrieved sucessfully"

            return JsonResponse({"status":"sucess","message":msg,"data":result,"total no of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
    

@csrf_exempt
def orderPlacing(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            order= OrderDetails.objects.create(
                   orderid=data["order_id"],
                   useremail=data["email"],
                   amount=data["amount"],
                   status=data["status"],
                   mode=data["mode"]
                )
            print(order.transaction_id)
            x=order.transaction_id
            
            return JsonResponse({
                "status":"sucess",
                "message":"payment details updates sucessfully ",
                "transaction_id":x
                }, status=201)
                          
        else:
            return JsonResponse({"error":"only post method is allowed"}, status=400)

    except Exception as e:
        return JsonResponse ({"error":"something went wrong"},status=500)
    
@csrf_exempt
def BookMyshow(request):
    try:
        if request.method == "POST":
            data=json.loads(request.body)
            MovieBooking.objects.create(moviename=data["movie_name"],showtime=data["show_time"],screenname=data["screen_name"])
            return JsonResponse({"status":"sucess","msg":"records inserted sucessfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})
    
@csrf_exempt
def Bookstore(request):
    try:
        if request.method == "POST":
            data=json.loads(request.body)
            Book.objects.create(bookname=data["Book_name"],author=data["author"],category=data["category"],price=data["price"],rating=data["rating"])
            return JsonResponse({"status":"sucess","msg":"records inserted sucessfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})