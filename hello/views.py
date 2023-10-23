from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def jarek(request):
    return HttpResponse("Hello, Jarek!")

def bob(request):
    return HttpResponse("Hello, Bob!")

def greet(request,name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
