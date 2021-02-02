from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registration(request):
    name = request.POST.get('name', 'default')
    password = request.POST.get('password','default')
    email = request.POST.get('email', 'default')
    return render(request, 'login.html')

def login(request):
    name = request.POST.get('name', 'default')
    password = request.POST.get('password', 'default')
    param = {'name':name, 'password':password}
    return render(request, "home.html", param)

def about(request):
    return HttpResponse("About me")