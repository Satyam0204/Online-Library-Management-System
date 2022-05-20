import imp
from pathlib import Path
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('customers/',views.customers,name='customers'),
    path('books/',views.books, name='books'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutpage,name='logout'),
    path('addreview/',views.createReview,name='addreview'),
    path('userpage/',views.userProfile,name='userpage')
    
]
