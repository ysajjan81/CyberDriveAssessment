from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        password = request.POST["password"]
        email = request.POST["email"]

        if User.objects.filter(email = email).exists():
            msg = "Email Address Already Exists !!!"
            messages.info(request, msg)
            param = {'message' : msg}
            return redirect('register')

        elif User.objects.filter(username = name).exists():
            msg = "Name Already Exists !!!"
            messages.info(request, msg)
            param = {'message' : msg}
            return redirect('register')
        else:
            user = User.objects.create_user(username=name, password=password, email=email)
            user.save()
            return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username = name, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            msg = "invalid credentials"
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
