import email
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):

    # getting the user information from front end and saving them in variables
    # to be accessed in code for connecting and playing with them in back-end
    if request.method=="POST":
        fname =request.POST.get('fname')
        lname =request.POST.get('lname')
        username =request.POST.get('username')
        email =request.POST.get('email')
        pass1  =request.POST.get('pass1')
        pass2  =request.POST.get('pass2')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request, "Your account has been created successfully, Thanks for registring on Event+")
        # redirect user to login page after regiatred
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    # sign in 
    if request.method=="POST":
        username =request.POST.get('uname')
        pass1  =request.POST.get('psw')

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html", {'fname':fname})
        else:
            messages.error(request," Invalid Credintials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success( request, "Logged out from Event+")
    return redirect ('home')