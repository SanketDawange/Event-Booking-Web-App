from http.client import HTTPResponse
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import AllEvent
import math as Math

def isPassWeak(pass1):
    return len(pass1) <8
    

# Create your views here.
@csrf_exempt
def home(request):
    return render(request,"authentication/index.html")

@csrf_exempt
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

        # if pass word do not match
        if pass1 != pass2:
            messages.warning(request, "Password do not match")
            return redirect('signup')

        # if the username is already taken
        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already exist")
            return redirect('signup')

        
        # password verifcation
        if isPassWeak(pass1):
            messages.warning(request, "Password must be 8 characters long combination of symbols, lowercase & uppercase letters")
            return redirect('signup')

        # if new user is registering 
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request, "Your account has been created successfully, Thanks for registring on Event+")
        # redirect user to login page after regiatred
        return redirect('signin')

    return render(request, "authentication/signup.html")

@csrf_exempt
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
            messages.error(request, "Invalid Credintials")
            return redirect('home')

    return render(request, "authentication/signin.html")

@csrf_exempt
def signout(request):
    logout(request)
    messages.success( request, "Logged out from Event+")
    return redirect ('home')

@csrf_exempt
def liveevents(request):
    AllEvents = AllEvent.objects.all()
    context = {'events' : AllEvents}
    return render(request, "authentication/liveevents.html", context)

@csrf_exempt
def contact(request):
    return render(request, "authentication/contact.html")

@csrf_exempt
def myaccount(request):
    
    return render(request, "authentication/myaccount.html")

@csrf_exempt
def eventdescription(request, eventname):
    event = AllEvent.objects.get(event_name = eventname)
    name = event.event_name
    place = event.event_place
    description = event.event_description
    date = event.event_date
    total_seats = int(event.total_seats)
    if total_seats <0:
        total_seats = 0
    rows = [1]*int(Math.sqrt(total_seats))
    seats = rows
    s = int(Math.sqrt(total_seats))*int(Math.sqrt(total_seats))
    remaining = [1]*(total_seats - s)
    context = {'name' : name, 'place': place , 'description':description , 'rows': rows,'total_seats':total_seats , 'date': date , 'seats': seats, 'remaining':remaining}
    return render(request, "authentication/eventdescription.html", context)

@csrf_exempt
def success(request):
    return render(request, "authentication/success.html")

@csrf_exempt
def addSeats(request):
    eventname = request.POST['name']
    count = int(request.POST['count'])
    event = AllEvent.objects.get(event_name = eventname)
    event.total_seats -= count 
    event.save()
    return JsonResponse({"msg":"Success"})