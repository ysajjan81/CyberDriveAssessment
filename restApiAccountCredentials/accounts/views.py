from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
import  re
from rest_framework.authtoken.views import obtain_auth_token

from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User

# check email is valid or not
def is_valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False

# check password is valid or not
def is_valid_password(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        # print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        # print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        # print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        # print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        # print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        # print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

# Endpoint for user registration
def register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        password = request.POST["password"]
        email = request.POST["email"]

        if not is_valid_email(email):
            msg = "Invalid Email Address !!!"
            messages.info(request, msg)
            return redirect('register')

        elif User.objects.filter(email = email).exists():
            msg = "Email Address Already Exists !!!"
            messages.info(request, msg)
            return redirect('register')

        elif not is_valid_password(password):
            msg = "Invalid Password !!!"
            messages.info(request, msg)
            return redirect('register')

        elif User.objects.filter(username = name).exists():
            msg = "Name Already Exists !!!"
            messages.info(request, msg)
            return redirect('register')
        else:
            user = User.objects.create_user(username=name, password=password, email=email)
            user.save()
            return redirect('/')
    else:
        return render(request, 'register.html')

# this api get called for login check the username and password give access to page.
def login(request):
    # When Request is POST
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username = name, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/', 'gettoken')

        else:
            msg = "invalid credentials"
            messages.info(request, 'invalid credentials')
            return redirect('login')

    # Request is GET just return the login page
    else:
        return render(request, 'login.html')

# End the session and return to home page.
def logout(request):
    auth.logout(request)
    return redirect('/')

# reset the password. Check the old password
def resetpassword(request):
    if request.method == 'GET':
        return render(request, 'resetpassword.html')
    else:
        name = None
        if request.user.is_authenticated:
            name = request.user.username

        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        user = auth.authenticate(username = name, password = oldpassword)

        if user is not None:
            # print("password exist")
            if newpassword == confirmpassword:
                # update password in db
                if is_valid_password(newpassword) == True:
                    u = User.objects.get(username = name)
                    u.set_password(newpassword)
                    u.save()
                    return redirect('login')
                else:
                    msg = "Invalid Password"
                    messages.info(request, msg)
                    return redirect('resetpassword')
            else:
                msg = "Password not matching"
                messages.info(request, msg)
                return redirect('resetpassword')
        else:
            msg = "password not exist !!!"
            messages.info(request, msg)
            return redirect('resetpassword')


def resetusername(request):
    if request.method == 'GET':
        return render(request, 'resetusername.html')
    else:
        currentName = None
        if request.user.is_authenticated:
            currentName = request.user.username
        print(currentName)

        newUserName = request.POST['newusername']
        password = request.POST['password']
        print("new user = ", newUserName)
        print("pass = ", password)

        user = auth.authenticate(username = currentName, password = password)
        if user is not None:
            u = User.objects.get(username=currentName)
            u.username = newUserName
            u.save()
            return redirect('/')
        return redirect('/')

# Endpoint to reset email
def resetemail(request):
    if request.method == "GET":
        return render(request, "resetemail.html")
    else:
        currentName = None
        if request.user.is_authenticated:
            currentName = request.user.username
        print(currentName)

        newEmail = request.POST['newemail']
        password = request.POST['password']
        print("new email = ", newEmail)
        print("password = ", password)

        user = auth.authenticate(username = currentName, password = password)
        if user is not None:
            print("Exist user and password")
            if not is_valid_email(newEmail):
                msg = "invalid Email !!!"
                messages.info(request, msg)
                return redirect('resetemail')

            u = User.objects.get(username=currentName)
            u.email = newEmail
            u.save()
            return redirect('/')
        else:
            msg = "invalid Password!!!"
            messages.info(request, msg)
            return redirect('resetemail')

# receiver learning something new Signals.
def login_success(sender, request, user,  **kwargs):
    print("_--------------------")
    print("logged out Signal ..... Run intro")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f'Kwargs: {kwargs}')

def logout_success(sender, request, user,  **kwargs):
    print("_--------------------")
    print("logged in Signal ..... Run intro")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f'Kwargs: {kwargs}')

user_logged_in.connect(login_success, sender=User)
user_logged_out.connect(logout_success, sender=User)