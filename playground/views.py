from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate():
    x=1
    y=2
    return x

def say_hello(request):
    #pull data from db
    #Transform
    #send email
    x=calculate()
    y=2
    return render(request,"hello.html",{"name":"Rahal"})
