from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import userProfile,Employee
from django.db.utils import IntegrityError

# Create your views here.
def home(request):
    return render(request,'home.html')
def sample(request):
    return HttpResponse("hello")

def sample1(request):
    info={"data" :[{"name":"Nikhil","city":"hyd","Gender":"M"},{"name":"Riya","city":"knr","Gender":"F"},{"name":"Riyansh","city":"Jgl","Gender":"M"}]}
    return JsonResponse(info)

# dynamic response using query params
def productInfo(request):
    product_name = request.GET.get("product",'mobile')
    quantity = int(request.GET.get("quality",1))
    price = int(request.GET.get("price",25000))
    data={"product":product_name, "quantity":quantity,"price":price,"totalprice":price*quantity}
    return JsonResponse(data)

# filtering using query params
def filteringData(request):
    data=[1,2,3,4,5,6,7,8,9,10]
    filteredData=[]
 
    qp=int(request.GET.get("num",2))

    for x in data:
        if x%qp==0:
            filteredData.append(x)
    
    return JsonResponse({"data":filteredData})

students_data = [{'name':'Raj','city':'hyd'},{'name':'Ram','city':'hyd'},{'name':'Ravi','city':'bgr'},{'name':'Raki','city':'bgr'}]

def filterStudentsByCity(request):
    filteredStudents=[]
    city=request.GET.get("city","hyd")

    for student in students_data:
        if student["city"] == city:
            filteredStudents.append(student)
    return JsonResponse({"status":"sucess","data":filteredStudents})


def pagination(request):
    data=['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry','dragonfruit']
    page =int(request.GET.get("page",1))
    limit =int(request.GET.get("limit",3))

    start=(page-1)*limit
    end=page*limit
    total_pages=math.ceil(len(data)/limit)
    result = data[start:end]

    res={"status":"sucess","current_page":page,"total_pages":total_pages,"data":result}
    return JsonResponse(res,status=302)
    
@csrf_exempt
def createData(request):
    try:
        if request.method =="POST":
            data=json.loads(request.body)
            name=data.get("name")
            age=data.get("age")
            city=data.get("city")
            userProfile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"sucess","data":data,"statuscode":201},status=201)   
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})


@csrf_exempt
def createProduct(request):
    if request.method =="POST":
        data=json.loads(request.body)
        print(data)
    return JsonResponse({"status":"sucess","data":data,"statuscode":201})

@csrf_exempt
def createEmployee(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            print(data)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("sal"),emp_email=data.get("email"))
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201) 
    except IntegrityError as e:
        return JsonResponse({"status":"error","message":"inputs are invalid or acceptable"},status=400)
    finally:
        print("done")