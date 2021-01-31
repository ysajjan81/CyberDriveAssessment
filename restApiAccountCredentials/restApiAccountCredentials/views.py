from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registration(request):
    name = request.GET.get('name', 'default')
    password = request.GET.get('password','default')
    email = request.GET.get('email', 'default')
    return HttpResponse("Hi " + name + "your email is: " + email)

def about(request):
    return HttpResponse("About me")