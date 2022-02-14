from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def addemployee(request):
    print("add employee called...")
    return HttpResponse("add employee called...")

#create views for display employee page
def viewemployee(request):
    return HttpResponse("view employee called....")

#create view employee function to display the product page
def employeepage(request):
    return render(request, 'employee/employeepage.html')