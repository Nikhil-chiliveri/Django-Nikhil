from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

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
    