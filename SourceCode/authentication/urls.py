from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('liveevents', views.liveevents, name ='liveevents'),
    path('contact', views.contact, name ='contact'),
    path('myaccount', views.myaccount, name ='myaccount'),
    path('eventdescription/<str:eventname>/', views.eventdescription, name ='eventdescription'),
    path('success', views.success, name ='success'),
    path('addSeats', views.addSeats, name ='addSeats'),
]